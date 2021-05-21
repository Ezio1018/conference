<template>
    <el-container class="home-container">
        <el-header>会议室
            <template>
                <el-dropdown class="profileLoc" @command="handleCommand">
                        <span class="el-dropdown-link">
                            <img src="../../src/assets/我的.png"/>
                            <i class="el-icon-arrow-down el-icon--right"></i>
                        </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item style="font-size:20px" command="a">查看个人信息</el-dropdown-item>
                        <el-dropdown-item style="font-size:20px" command="b">退出</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </template>
        </el-header>
        <el-container>
            <el-aside width="200px" style="background:rgba(255,255,255,0.5);">
                <el-card>
                    <el-menu v-on:unique-opened="true"
                             background-color=""
                             text-color="black"
                             active-text-color="blue" unique-opened router><!--这个是选中的时候显示的颜色-->
                        <el-menu-item index="/firsthop" @click="saveNavState('/'+$route.path)">
                            <i class="el-icon-menu"></i>
                            <span slot="title" >首页</span>
                        </el-menu-item>
                      <el-menu-item index="/userMana" @click="saveNavState('/'+$route.path)" v-show ="this.manashow">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >用户管理</span>
                      </el-menu-item>
                      <el-menu-item index="/conferenceMana" @click="saveNavState('/'+$route.path)" v-show = "this.manashow">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >会议室管理</span>
                      </el-menu-item>
                      <el-menu-item index="/conferenceBook" @click="saveNavState('/'+$route.path)" v-show = "this.usershow">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >会议室预定</span>
                      </el-menu-item>
                      <el-menu-item index="/staff" @click="saveNavState('/'+$route.path)" v-show = "this.staffshow">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >后勤任务</span>
                      </el-menu-item>
                      <el-menu-item index="/formshow" @click="saveNavState('/'+$route.path)" v-show = "this.usershow || this.staffshow">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >参加会议记录</span>
                      </el-menu-item>
                      <el-menu-item index="/checkform" @click="saveNavState('/'+$route.path)" v-show = "this.usershow">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >查看已预约会议室</span>
                      </el-menu-item>
                    </el-menu>
                </el-card>

            </el-aside>
            <el-container >
                <el-main style="background:rgba(255,255,255,0.5);">
                    <!--路由占位符-->
                    <!--在router的index.js里面实现，这里跳转到firsthop页面-->
                    <el-card>
                        <router-view></router-view>
                    </el-card>
                </el-main>
            </el-container>
        </el-container>
    </el-container>

</template>
<script>
export default {
  // created(){
  //     if(this.GLOBAL.currentUser.role_name==="管理员")
  //     {
  //         this.entranceForAdmin=false;
  //     }
  //     else if(this.GLOBAL.currentUser.role_name==="教师")
  //     {
  //         this.entranceForTeacher=false;
  //     }
  //     else if(this.GLOBAL.currentUser.role_name==="学生")
  //     {
  //         this.entranceForStu=false;
  //     }
  // },
  name: 'home',
  data () {
    return {
      manashow: false,
      usershow: false,
      staffshow: false,
      identity : "",
      // entranceForTeacher:true,//true表示没法访问
      // entranceForAdmin:true,
      // entranceForStu:true,
    }
  },
  created(){
    if(localStorage.identity === "admin")
      this.manashow = true;
    else if(localStorage.identity === "user")
      this.usershow = true;
    else
      this.staffshow = true;
    console.log(this.manashow)
    console.log(this.usershow)
  },
  methods: {
    handleCommand (command) {
      if (command === 'a') {
        this.$router.push('/profile')// 为路由提供地址
      }
      if (command === 'b') {
        this.logout()
        this.$message('您已退出')
      }
    },
    logout () {
      window.sessionStorage.clear()// 删除这个token
      this.$router.push('/login')// 返回登录界面
    },
    // 保存链接的激活状态
    saveNavState (activepath){ // 为每一个按钮添加，按下去的时候会在Application里面加入一个activepath
      window.sessionStorage.setItem('activepath', activepath)// 用来保存当前访问的路径
    }
    // 请求左侧菜单
    // async getMenuList(){
    //     const { data: res } = await this.$http.get('menus')
    //     console.log(res);
    // }
  }
}
</script>

<style scoped>
    .el-header{
        background-color: white;
        font-size:20px;

    }
    .el-aside{
        background: linear-gradient(135deg,white,white);
    }
    .el-menu{
        border-right:none;/*解决2级菜单突出来的情况*/
    }
    .el-main{
        background-color: white;
    }
    .home-container{
        height: 100vh;
        background: url('../../src/assets/nastuh-abootalebi-eHD8Y1Znfpk-unsplash.jpg')  no-repeat scroll top right  #aaa9a7;
        background-size: cover;

    }
    .el-header{
        font-family :"幼圆";
        font-size :40px;
    }
    .profileLoc{
        position:absolute;/*可以用坐标标记*/
        top: 0.5%;
        right: 1%;
    }
    .el-dropdown-link {

        cursor: pointer;
        color: white;
    }
    .el-icon-arrow-down {
        font-size: 25px;
    }
</style>
