<template>
	<div>
		<el-col :span="24" class="upload_img">
			<el-col :span="12">
				<el-col :span="4"><span>拍照上传</span></el-col>
				<el-button @click="onTake" icon="el-icon-camera" size="small">
					拍照上传
				</el-button>
			</el-col>
		</el-col>
		<el-col :span="24">
			<el-col :span="12">
				<el-col :offset="4">
					<el-image style="width: 100px; height: 100px" v-if="imgUrl" :src="'http://' + imgUrl" :fit="fit">
					</el-image>
				</el-col>
			</el-col>
		</el-col>
		<el-dialog title="拍照上传" :visible.sync="visible" @close="onCancel" width="1065px">
			<div class="box">
				<video id="videoCamera" class="canvas" ref="video" :width="videoWidth" :height="videoHeight" autoPlay></video>
				<canvas id="canvasCamera" class="canvas" ref="canvas" :width="videoWidth" :height="videoHeight"></canvas>
			</div>
			<div slot="footer">
				<el-button @click="drawImage" icon="el-icon-camera" size="small">
					拍照
				</el-button>
				<el-button v-if="open" @click="getCompetence" icon="el-icon-video-camera" size="small">
					打开摄像头
				</el-button>
				<el-button v-else @click="stopNavigator" icon="el-icon-switch-button" size="small">
					关闭摄像头
				</el-button>
				<el-button @click="resetCanvas" icon="el-icon-refresh" size="small">
					重置
				</el-button>
				<el-button @click="onCancel" icon="el-icon-circle-close" size="small">
					取消
				</el-button>

			</div>
		</el-dialog>
	</div>
</template>
<script>
	//拍照上传组件

	export default {

		name: "upload",
		data() {
			return {
				// imgUrl: '', //后端给返回的图片地址
				imgSrc: '', // base64的图片格式
				visible: false, //弹窗
				loading: false, //上传按钮加载
				open: false, //控制摄像头开关
				thisVideo: null,
				thisContext: null,
				thisCancas: null,
				videoWidth: 500,
				videoHeight: 400,
				front: true,
				fit: 'none',
				fileList: []
			}
		},
		methods: {
			onTake() {
				this.visible = true;
				this.getCompetence();
			},
			onCancel() {
				this.visible = false;
				this.resetCanvas();
				this.stopNavigator();
			},
			//base64转成文件后上传
			onUpload() {
				if (this.imgSrc) {
					const file = this.imgSrc; // 把整个base64给file
					const time = (new Date()).valueOf(); //生成时间戳
					const name = time + ".png"; // 定义文件名字（例如：abc.png ， cover.png）

					const conversions = this.dataURLtoFile(file, name); // 调用base64转图片方法
					const data = new FormData();
					data.append('picture', conversions);
					this.loading = true;
					// axios接口
					suppPic(data).then(res => {
						if (res.data) this.$message({
							message: '保存成功',
							type: 'success'
						})
						this.loading = false
						this.imgUrl = 'http://' + res.data
						this.onCancel()
						this.$emit('imgObj', {
							upload: true,
							imgsrc: res.data
						})
					})

				} else {
					this.$message({
						message: '请点击拍照',
						error: 'warning'
					});
				}
			},
			// 调用摄像头权限

	getCompetence () {
      // H5调用电脑摄像头API
      navigator.mediaDevices.getUserMedia({
        video: true
      }).then(success => {
        // 摄像头开启成功
        this.$refs['video'].srcObject = success
        // 实时拍照效果
        this.$refs['video'].play()
      }).catch(error => {
        console.error('摄像头开启失败，请检查摄像头是否可用！')
      })
    },
			//绘制图片
	drawImage() {
      let ctx = this.$refs['canvas'].getContext('2d')
      // 把当前视频帧内容渲染到canvas上
      ctx.drawImage(this.$refs['video'], 0, 0, 640, 480)
      // 转base64格式、图片格式转换、图片质量压缩
      let imgBase64 = this.$refs['canvas'].toDataURL('image/jpeg')

// 　　　 // 由字节转换为KB 判断大小
//       let str = imgBase64.replace('data:image/jpeg;base64,', '')
//       let strLength = str.length
//       let fileLength = parseInt(strLength - (strLength / 8) * 2)
// 　　　 // 图片尺寸  用于判断
//       let size = (fileLength / 1024).toFixed(2)
    //   console.log(size)
	let formData = new FormData();
	formData.append('test_image',imgBase64);
	this.name=this.$route.query.name;//接收参数
	formData.append('id',this.name)
	 this.$axios.post('/apis/api/detect', formData
            )
			.then(response => {
                if (response.data.status === 0) {
                  this.$notify({
                    title: '人脸识别成功',
                    message: response.data.message,
                    type: 'sucess'
                  })
          this.$router.push({path: '/home',
          query: { name: this.name}});
                  window.location.reload();
                } else if(response.data.status === 1){
					this.$notify({
                    title: '未识别出人脸，换个角度拍照',
                    message: response.data.message,
                    type: 'error'
                  })
                }
				else{
					this.$notify({
                    title: '人脸识别失败',
                    message: response.data.message,
                    type: 'error'
                  })
				}
              })

    },
			//清空画布
			clearCanvas(id) {
				let c = document.getElementById(id);
				let cxt = c.getContext("2d");
				cxt.clearRect(0, 0, c.width, c.height);
			},
			//重置画布
			resetCanvas() {
				this.imgSrc = "";
				this.clearCanvas('canvasCamera');
			},
			//关闭摄像头
			stopNavigator() {
				if (this.thisVideo && this.thisVideo !== null) {
					this.thisVideo.srcObject.getTracks()[0].stop();
					this.open = true; //切换成打开摄像头
				}
			},
		},
		beforeDestroy() {
			this.stopNavigator()
		},

		props: {
			imgUrl: String
		}
	}
</script>
