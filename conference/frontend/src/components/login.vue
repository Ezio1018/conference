<template>
   <div class="homepage-hero-module">
        <div class="video-container">
          <div  class="filter">
         <div class="login_container">
        <div class="login_box">
            <!--ref="loginformref1"是引用对象名-->
            <!--            <h2 class="color:white;position:absolute;left: 50%;">登  录</h2>-->
            <el-form class="radio_role">
                <el-radio  v-model="role" label="1">管理员</el-radio>
                <el-radio  v-model="role" label="2">用户</el-radio>
                <el-radio  v-model="role" label="3">后勤</el-radio>
            </el-form>
            <el-form ref="loginFormRef1" :model="loginform" :rules="loginformrules" label-width="80px"  class="login_form"><!--动态绑定sername-->
                <el-form-item label="用户名" prop="userNumber" style="font-size:25px" placeholder="请输入用户名"><!--prop="userNumber"是指定用户规则-->
                    <el-input v-model="loginform.userNumber" style="width:350px;font-size: 20px;"></el-input>
                </el-form-item>
                <!--密码-->
                <el-form-item label="密码" prop="password" style="font-size:25px">
                    <el-input v-model="loginform.password" type="password" style="width:350px;font-size: 20px;"></el-input>
                </el-form-item>
                <!--按钮-->
                <el-form-item class="btns">
                    <el-button type="primary"  @click="addDialogVisible = true">注册</el-button>
                    <el-button type="primary" @click="login('loginFormRef1')">登录</el-button>
                    <el-button type="info" @click="resetloginform">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
        <!--注册的对话框-->
        <el-dialog
                title="注册"
                :visible.sync="addDialogVisible"
                width="40%"
                @close="addDialogClosed">
            <!--:before-close="handleClose">-->
            <!--内容主体区域,ref是引用对象名-->
            <el-form :model="addForm" :rules="addFormRules" ref="addFormRef" label-width="70px">
                <el-form-item label="用户姓名" placeholder="请输入姓名">
                    <el-input v-model="addForm.username"></el-input>
                </el-form-item>
                <el-form-item label="性别" >
                    <el-select v-model="addForm.gender" placeholder="请选择性别" style="display: block;">
                        <el-option label="男" value="m"></el-option>
                        <el-option label="女" value="w"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="用户id" placeholder="请输入账号" prop="userid">
                    <el-input v-model="addForm.userid"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password" placeholder="请输入密码">
                    <el-input type="password" v-model="addForm.password"></el-input>
                </el-form-item>
                 <el-form-item label="验证" prop="repassword">
                  <el-input type="password" v-model="addForm.repassword" placeholder="请再次输入密码"></el-input>
               </el-form-item>
                  <el-form-item label="角色" >
                    <el-select v-model="addForm.role_name" placeholder="请选择角色" style="display: block;">
                        <el-option label="用户" value="user"></el-option>
                        <el-option label="后勤" value="staff"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="部门" prop="college">
                    <el-select v-model="addForm.college" placeholder="请选择部门" style="display: block;">
                        <el-option label="技术部" value="技术部"></el-option>
                        <el-option label="推广部" value="推广部"></el-option>
                        <el-option label="客服部" value="客服部"></el-option>
                        <el-option label="行政部" value="行政部"></el-option>
                        <el-option label="财务部" value="财务部"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="邮箱" prop="email" placeholder="请输入邮箱">
                    <el-input v-model="addForm.email"></el-input>
                </el-form-item>
                <el-form-item label="头像" prop="image">
                   <input type="file" @change="getImageFile">
                </el-form-item>

            </el-form>
            <!--底部按钮区-->
            <span slot="footer" class="dialog-footer">
                <el-button @click="addDialogVisible = false">取 消</el-button><!--点击取消隐藏对话框-->
                <el-button type="primary" @click="submit">确 定</el-button><!--点击确定也会隐藏对话框-->
            </span>
        </el-dialog>
       </div>
          </div>
          <video  autoplay loop muted class="fillWidth" v-on:canplay="canplay">
            <source src="../assets/video1.mp4" type="video/mp4"/>
            浏览器不支持 video 标签，建议升级浏览器。
            <!-- <source src="../assets/G1w.webm" type="video/webm"/>
            浏览器不支持 video 标签，建议升级浏览器。 -->
          </video>
          <!-- <div class="poster hidden" v-if="!vedioCanPlay">
            <img :style="fixStyle" src="../assets/G1.jpg" alt="">
          </div> -->
        </div>
      </div>

</template>
<script>
    export default {
        data(){

        var checkPassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'))
        } else if (value !== this.addForm.password) {
          callback(new Error('两次输入的密码不一致.'))
        } else {
          callback()
        }
        }
         var dulaUsername = (rule, value, callback) => {
        // 验证用户名是否存在.  一会再写
        if (value.length < 3) {
          callback(new Error('你的用户名太短了！'))
        } else if (value.length > 18) {
          callback(new Error('你的用户名太长了！'))
        } else {
          let formData = new FormData();
            formData.append('select_username', value);
          this.$axios.post('/apis/api/register?select=1', formData)
            .then(response => {
              if (response.data.is_indb === 1) {
                callback(new Error('该用户名已经被注册'))
              } else {
                callback();
              }
            })
        }
        }

           var checkEmail = (rule, value, cb) => {
          // 验证邮箱的正则表达式
          const regEmail = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;
            if (regEmail.test(value)) {
        // 合法的邮箱
            return cb();
              }
          cb(new Error("请输入合法的邮箱"));
             };

            return{
                role:'1',
                //这是登录表单的数据绑定对象
                loginform:{
                    userNumber:'',
                    password:"",
                },
                //表单的验证规则对象
                loginformrules:{
                    userNumber:[
                        { required: true, message: '请输入用户名', trigger: 'blur' }
                    ],
                    password:[
                        { required: true, message: '请输入密码', trigger: 'blur' }
                    ]
                },
                addForm:{
                  username: "",
                  userid:"",
                  password: "",
                  repassword: "",
                  email: "",
                  college:"",
                  gender:"",
                  department:"",
                  image:'',
                  role_name:'',
                },
                addDialogVisible:false,
                addFormRules: {
                    userid: [
                        //不知道为啥，下面这行有点问题，怎么输出都输出请输入用户名
                        {required: true, message: '请输入账户', trigger: 'blur'},//鼠标移开不填的情况
                        {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'},
                        {validator: dulaUsername, trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '请输入密码', trigger: 'blur'},//鼠标移开不填的情况
                        {min: 6, max: 15, message: '长度在 6 到 15 个字符之间', trigger: 'blur'}
                    ],
                    email: [
                        {required: true, message: '请输入邮箱', trigger: 'blur'},//鼠标移开不填的情况
                        {validator: checkEmail, trigger: 'blur'}
                    ],
                    mobile: [
                        {required: true, message: '请输入手机号', trigger: 'blur'},//鼠标移开不填的情况
                        // {validator: checkMobile, trigger: 'blur'}//上面定义的正则表达式
                    ],
                    repassword: [
                        {required: true, message: '请再次输入密码', trigger: 'blur'},//鼠标移开不填的情况
                        {validator: checkPassword, trigger: 'blur'}

                    ],
                },//添加表单的验证规则对象
            };
        },
        methods: {
      getImageFile:function(e) {
         let file = e.target.files[0];
         this.addForm.image = file;
      },
        resetloginform(){
                // console.log(this);//打印的是这个组件的实例
                this.$refs.loginFormRef1.resetFields();
            },
        submit(){
          console.log(this.addForm.image)
        this.$refs.addFormRef.validate((valid) => {
          if (valid) {

             let formData = new FormData();
              formData.append('name', this.addForm.username);
              formData.append('userid', this.addForm.userid);
              formData.append('password', this.addForm.password);
              formData.append('email', this.addForm.email);
              formData.append('gender', this.addForm.gender);
              formData.append('department', this.addForm.college);
              formData.append('image', this.addForm.image);
              formData.append('identity', this.addForm.role_name);

            // 成功.
            this.$axios.post('/apis/api/register', formData
            )
              .then(response => {
                if (response.data.status === 0) {
                  this.$notify({
                    title: '注册成功',
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

        login: function (Dataset) {
        this.$refs[Dataset].validate((valid) => {
          if (valid) {
            // 成功
            this.$axios.post("apis/api/login", {
              username: this.loginform.userNumber,
              password: this.loginform.password,
            })
              .then(response => {
                if (response.data.status === 0) {
                  this.$router.push({path: '/face',
                  query: { name: this.loginform.userNumber }});
                  localStorage.user_id = this.loginform.userNumber
                  localStorage.identity = response.data.identity
                  localStorage.user_name = response.data.username
                  window.location.reload();
                } else {
                  this.$notify({
                    title: '登录失败',
                    message: response.data.message,
                    type: 'error'
                  })
                }
              })
          } else {
            return false;
          }
        })
      },
      canplay() {
        this.vedioCanPlay = true
      }
    },
};
</script>

<style scoped>
    h1 {
        color:white;
        font-size:40px;
        position:absolute;/*可以用坐标标记*/
        left: 50%;
        top: 25%;
        transform: translate(-50%, -50%);/*放置到正中间*/
    }
    h2 {
        color:white;
        position:absolute;/*可以用坐标标记*/
        left: 50%;
        top: 30%;
        transform: translate(-50%, -50%);/*放置到正中间*/
    }
    .login_container{
        /* background: url('../../src/assets/nbu2.jpg')  no-repeat scroll top right  #D5CCBD; */
        background-size: cover;
        height:100vh;
    }

    /*登陆的那个框框*/
    .login_box{
        width:500px;
        height:330px;
        /* background-color: rgba(43, 35, 35, 0.7); */
        border-radius: 3px;
        position:absolute;/*可以用坐标标记*/
        left: 50%;
        top: 55%;
        transform: translate(-50%, -50%);/*放置到正中间*/
        background: rgba(24, 20, 20, 0.7);
	      box-sizing: border-box;
	      box-shadow: 0 15px 25px rgba(0,0,0,.5);
      	border-radius: 10px;
    }
    .radio_role{
        position:absolute;/*可以用坐标标记*/
        left: 50%;
        top: 22%;
        transform: translate(-50%, -50%);/*放置到正中间*/
    }
    .btns{
        position:absolute;/*可以用坐标标记*/
        left: 28%;
        top: 55%;
        display: flex;/*水平居于有对齐*/
        justify-content: flex-end;
    }
    .login_form{
        position:absolute;
        top:30%;
        bottom:0;
        width:100%;
        padding:0 20px;
        box-sizing:border-box;
    }


 .homepage-hero-module,
.video-container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.video-container .poster img{
  z-index: 0;
  position: absolute;
}

.video-container .filter {
  z-index: 1;
  position: absolute;
  background: rgba(0, 0, 0, 0.013);
  width: 100%;
}

.fillWidth {
  width: 100%;
}
</style>
