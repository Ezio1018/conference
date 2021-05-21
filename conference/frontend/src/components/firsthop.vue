<template >
    <div class="mainClass">
        <el-card>
            <el-button type="primary" @click="addDialogVisible = true">报修</el-button>
        </el-card>
      <el-calendar class="rili">
      <template
        slot="dateCell"
        slot-scope="{data}">
        <p :class="data.isSelected ? 'is-selected' : ''">
          {{ data.day.split('-').slice(1).join('-') }}
        </p>
        <template v-for="item in events">
<!--          {{data.date}}-->
          <span style="color:#FF6666" :key="item.day" v-if="data.day===item.day">
                      {{ item.room}}({{ item.time_id == 1 ? '1:00 - 2:00' : item.time_id == 2 ? '2:00 - 3:00': item.time_id == 3 ? '3:00 - 4:00' : item.time_id == 4 ? '10:00 - 11:00':  item.time_id == 5 ? '11:00 - 12:00':''}})</span>
        </template>
      </template>
    </el-calendar>
        <el-dialog
            title="后勤"
            :visible.sync="addDialogVisible"
            width="40%"
            @close="addDialogClosed">
        <!--:before-close="handleClose">-->
        <!--内容主体区域,ref是引用对象名-->
        <el-form :model="addForm" :rules="addFormRules" ref="addFormRef" label-width="70px">
            <el-form-item label="用户id" placeholder="请输入任务编号" prop="userid">
                <el-input v-model="addForm.userid"></el-input>
            </el-form-item>
            <el-form-item label="会议室" placeholder="请输入会议室" prop="conference">
                <el-input v-model="addForm.conference"></el-input>
            </el-form-item>
            <el-form-item label="服务类型"  prop="service">
                <el-select v-model="addForm.service" placeholder="请选择服务类型" style="display: block;">
                    <el-option label="报修" value="报修"></el-option>
                    <el-option label="清洁" value="清洁"></el-option>
                    <el-option label="布置" value="布置"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="内容" placeholder="请输入具体内容" prop="content">
                <el-input v-model="addForm.content"></el-input>
            </el-form-item>
        </el-form>
        <!--底部按钮区-->
        <span slot="footer" class="dialog-footer">
            <el-button @click="addDialogVisible = false">取 消</el-button><!--点击取消隐藏对话框-->
            <el-button type="primary" @click="submit">确 定</el-button><!--点击确定也会隐藏对话框-->
        </span>
    </el-dialog>
    </div>

</template>

<script>
    export default {
        data(){
            return{
                addForm:{
                 service:'',
                 conference:'',
                 userid:'',
                 content:"",
                },
                value: new Date(),
                month: "05-15",
                events:[],
                addDialogVisible:false,
            };
        },
    created(){
      this.user_id = localStorage.user_id
      this.showForms()
    },
        methods: {
        showForms () {
        this.$http.get('http://127.0.0.1:8000/api/show_meeting?user_id=' + this.user_id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num === 0) {
              this.events = JSON.parse(res['list'])
   
            } else {
              this.$message.error('查询预约失败')

            }
          })
      },
        submit(){
        this.$refs.addFormRef.validate((valid) => {
          if (valid) {
             let formData = new FormData();
              formData.append('userid', this.addForm.userid);
              formData.append('conference', this.addForm.conference);
              formData.append('service', this.addForm.service);
              formData.append('content', this.addForm.content);
            // 成功.
            this.$axios.post('/apis/hq/baoxiu', formData
            )
              .then(response => {
                if (response.data.status === 0) {
                  this.$notify({
                    title: '提交成功',
                    message: response.data.message,
                    type: 'sucess'
                  })
                } else {
                  return false
                }
              })
          } else {
            return false;
          }
        });
      },
    addDialogClosed(){
            this.$refs.addFormRef.resetFields()
        },
}
}

</script>

<style scoped>
  .rili{
    width:1000px;
    height:700px;

  }

  .el-carousel__item:nth-child(2n) {
    background-color: white
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: white;
  }
  .el-carousel__indicator .el-carousel__button {
    background: #959595;
    border-radius: 50%;
    height: 14px;
    width: 14px;
  }
  .el-carousel__indicator.is-active .el-carousel__button {
    background: white;
  }
  .el-cardCss{
    width:1200px;
    height:750px;
    position:absolute;/*可以用坐标标记*/
    left: 55%;
    top: 55%;
    background-color: rgba(255,255,255,0.6);
    transform: translate(-50%, -50%);/*放置到正中间*/
  }
  .is-selected {
    color: #1989FA;
  }
</style>
