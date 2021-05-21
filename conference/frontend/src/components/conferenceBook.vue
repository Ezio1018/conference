<template>

<div class="home">
  <div class="block">
    <span class="demonstration"></span>
    <el-carousel type="card" height="350px" width="200px">
      <el-carousel-item v-for="item in imgList" :key="item.name">
        <el-image :src="item.src" style="height:100%;width:100%;" alt="图片丢失了" :title="item.title" fit="cover" :preview-src-list="imgeList" />
        <h3 class="small">{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
  </div>
<el-row display="margin-top:10px">
<!--el-input v-model="input" placeholder="请输入会议室编号" style="display:inline-table; width: 30%; float:left"></el-input>
<el-button type="primary" @click="addConference()" style="float:left; margin: 2px;">新增</el-button-->
<el-input v-model="input_conference_id" placeholder="请输入搜索会议室编号" style="display:inline-table; width: 30%; float:left"></el-input>
<el-button type="primary" @click="showConferences()" style="float:left; margin: 2px;">搜索</el-button>
<el-button @click="Changed(0)" v-trigger>{{updateTime}}</el-button>

<el-select v-model="value" placeholder="请选择" @change="Changed(value)">
            <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
            </el-option>
        </el-select>
</el-row>
<el-row>
<el-table :data="conferenceList" style="width: 1000%" border>
  <el-table-column prop="conference_id" label="编号" min-width="100">
  <template slot-scope="scope"> {{ scope.row.pk }} </template>
  </el-table-column>
  <el-table-column prop="conference_capacity" label="容量" min-width="100">
  <template slot-scope="scope"> {{ scope.row.fields.conference_capacity }} </template>
  </el-table-column>
  <el-table-column prop="conference_capacity" label="10:00-11:00" min-width="100">
  <template slot-scope="scope" ><!--作用域插槽-->
      <div id="app">
    <el-button size="mini" :type="way(scope.row.pk,4,scope.row.fields.conference_status)" :icon= "way1(bookway(scope.row.pk,4))" @click="addPeople(scope.row.pk,bookway(scope.row.pk,4,scope.row.fields.conference_status),4,'10:00-11:00',scope.row.fields.conference_capacity)">{{bookway(scope.row.pk,4,scope.row.fields.conference_status)}}</el-button>
      </div>
      </template>
  </el-table-column>
  <el-table-column prop="conference_capacity" label="11:00-12:00" min-width="100">
  <template slot-scope="scope" ><!--作用域插槽-->
      <div id="app">
    <el-button size="mini" :type="way(scope.row.pk,5,scope.row.fields.conference_status)" :icon= "way1(bookway(scope.row.pk,5))" @click="addPeople(scope.row.pk,bookway(scope.row.pk,5,scope.row.fields.conference_status),5,'11:00-12:00',scope.row.fields.conference_capacity)">{{bookway(scope.row.pk,5,scope.row.fields.conference_status)}}</el-button>
      </div>
      </template>
  </el-table-column>
  <el-table-column prop="conference_capacity" label="1:00-2:00" min-width="100">
  <template slot-scope="scope" ><!--作用域插槽-->
      <div id="app">
    <el-button size="mini" :type="way(scope.row.pk,1,scope.row.fields.conference_status)" :icon= "way1(bookway(scope.row.pk,1))" @click="addPeople(scope.row.pk,bookway(scope.row.pk,1,scope.row.fields.conference_status),1,'1:00-2:00',scope.row.fields.conference_capacity)" >{{bookway(scope.row.pk,1,scope.row.fields.conference_status)}}</el-button>
    
      </div>
      </template>
  
  </el-table-column>
  <el-table-column prop="conference_capacity" label="2:00-3:00" min-width="100">
  <template slot-scope="scope" ><!--作用域插槽-->
      <div id="app">
    <el-button size="mini" :type="way(scope.row.pk,2,scope.row.fields.conference_status)" :icon= "way1(bookway(scope.row.pk,2))" @click="addPeople(scope.row.pk,bookway(scope.row.pk,2,scope.row.fields.conference_status),2,'2:00-3:00',scope.row.fields.conference_capacity)">{{bookway(scope.row.pk,2,scope.row.fields.conference_status)}}</el-button>
      </div>
      </template>
  </el-table-column>
  <el-table-column prop="conference_capacity" label="3:00-4:00" min-width="100">
  <template slot-scope="scope" ><!--作用域插槽-->
      <div id="app">
    <el-button size="mini" :type="way(scope.row.pk,3,scope.row.fields.conference_status)" :icon= "way1(bookway(scope.row.pk,3))" @click="addPeople(scope.row.pk,bookway(scope.row.pk,3,scope.row.fields.conference_status),3,'3:00-4:00',scope.row.fields.conference_capacity)">{{bookway(scope.row.pk,3,scope.row.fields.conference_status)}}</el-button>
    <!-- <el-button size="mini" :type="way(scope.row.pk,3,scope.row.fields.conference_status)" :icon= "way1(bookway(scope.row.pk,3))" @click="canhui()">{{bookway(scope.row.pk,3,scope.row.fields.conference_status)}}</el-button> -->
      </div>
      </template>
  </el-table-column>

</el-table>
  </el-row>

  <el-dialog
                title="添加记录"
                :visible.sync="addConferenceVisible"
                width="40%"
                @close="addConferenceVisible = false">
            <el-form ref="addFormRef" :model="addForm"  label-width="100px">
                <el-form-item label="会议室编号" prop="conference_id">
                    <div>{{now_conference_id}}</div>
                </el-form-item>
                <el-form-item label="预约时间" prop="conference_id">
                    <div>{{updateTime}}: {{show_time}}</div>
                </el-form-item>
                <el-form-item label="选择人员" prop="conference_id">
                <el-select v-model="value11" multiple placeholder="请选择" @change="Changedname(value11)">

                <el-option
                    v-for="item in name1"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
                </el-select>
                </el-form-item>
                <el-form-item label="已选择人数" prop="conference_id">
                  
                <div>{{name2.length}} 人
                <el-button @click="qingkong()" >重新选择</el-button> </div>
                </el-form-item>
                <!--el-form-item label="会议室容量" prop="conference_capacity">
                    <el-input v-model="addForm.conference_capacity" ></el-input>
                </el-form-item>
                <el-form-item label="会议室状态" prop="conference_status">
                    <el-input v-model="addForm.conference_status" ></el-input>
                </el-form-item>
                <el-form-item label="会议室权限" prop="conference_authorization">
                    <el-input v-model="addForm.conference_authorization" ></el-input>
                </el-form-item-->
            </el-form>
            <!--底部按钮区-->
            <span slot="footer" class="dialog-footer">
                <el-button @click="addConferenceVisible = false">取 消</el-button><!--点击取消隐藏对话框-->
                <el-button type="primary" @click="yyConference()">确 定</el-button><!--点击确定也会隐藏对话框-->
            </span>
        </el-dialog>




  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      imgeList: [
          require('@/components/conference1.jpg'),
          require('@/components/conference2.jpg'),
          require('@/components/conference3.jpg'),
          require('@/components/conference4.jpg')
        ],
      imgList: [
        {
          name: "lj",
          src: require("@/components/conference1.jpg"),
          title: "这是lj.png"
        },
        {
          name: "logo",
          src: require("@/components/conference2.jpg"),
          title: "这是logo.png"
        },
        {
          name: "bg",
          src: require("@/components/conference3.jpg"),
          title: "这是bg.png"
        },
        {
          name: "sadmas",
          src: require("@/components/conference4.jpg"),
          title: "这是sadmas.png"
        }
      ],
      addConferenceVisible: false,
      addForm: {},
      date: new Date(),
      showModal: false,
      updateTime:'',
      updateTime1:'',
      updateTime2:'',
      updateTime3:'',
      input: '',
      value11:'',
      input_conference_id: '',
      now_conference_id: '',
      now_time: '',
      delete_conference_id: '',
      conferenceList: [],
      selected: '',    
      name1:[],
      name2:'',
      user_id :'',
      truename :[],
      show_time:'',
      name_draw:'',
      formslist:[],      
      capcity_now:'',
      options: [
       {label:'今天',value:0},
       {label:'明天',value:1},
       {label:'后天',value:2},
       {label:'大后天',value:3}]
    }
  },

  mounted: function () {
    this.user_id = localStorage.user_id
    this.showConferences()
    this.showname()
    this.draw()
  },

  directives:{
    trigger:{
     inserted(el,binging){
        el.click()
       //$(el).trigger('click')
      }
   }
},

  methods: {
    addPeople (delid,a,b,c,capcity) {
      if(a=="已预约"){

        this.$message.error('预约会议室失败')   
      }
      else if(a=="正在维修"){
          this.$message.info('会议室正在维修中...')  
          
      }
      else{


      this.addConferenceVisible = true
      this.now_conference_id = delid
      this.now_time = b
      this.show_time =c
      this.capcity_now = capcity
      }
    },

    yyConference () {
      this.addConferenceVisible = false
      if(this.capcity_now<this.name2.length){
        this.$message.error('邀请人数超出会议室容量')
        return 
      }
      this.truename=[]
      for (var i=0;i<this.name2.length;i++){
            var t = this.name2[i]
            console.log(this.name_draw)
            this.truename.push(this.name_draw[t])

      }
     
      this.$http.get('http://127.0.0.1:8000/form/yy_conference?conference_id=' + this.now_conference_id+'&user_id='+this.user_id+'&time_id='+this.now_time+'&day='+this.updateTime+'&Participants='+this.truename)  //传的是会议室编号
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showConferences()
            this.draw()
          } else {
            this.$message.error('预约会议室失败')

          }
        })

    },
 
    showname(){
      this.$http.get('http://127.0.0.1:8000/form/show_name?user_id='+this.user_id)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          this.name_draw = res
          for (var i=0;i<res['length'];i++){
            this.name1.push({
              label:res[i],
              value:i,
            })
            }
        })
    },
    showConferences () {
      this.$http.get('http://127.0.0.1:8000/form/show_conference?conference_id=' + this.input_conference_id)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.conferenceList = res['list']
          } else {
            this.$message.error('查询会议室失败')
          }
        })
    },
    Changed(flag){
               
                if(flag=="0"){
                  const nowDate = new Date();
            const date = {
                year: nowDate.getFullYear(),
                month: nowDate.getMonth() + 1,
                date: nowDate.getDate(),
            }
            const newmonth = date.month>9?date.month:'0'+date.month
            const day = date.date>9?date.date:'0'+date.date
            this.updateTime = date.year + '-' + newmonth + '-' + day
                }
                else if(flag=="1"){
                  const nowDate = new Date();
            const date = {
                year: nowDate.getFullYear(),
                month: nowDate.getMonth() + 1,
                date: nowDate.getDate()+1,
            }
            const newmonth = date.month>9?date.month:'0'+date.month
            const day = date.date>9?date.date:'0'+date.date
            this.updateTime = date.year + '-' + newmonth + '-' + day
                }
                else if(flag=="2"){
                  const nowDate = new Date();
            const date = {
                year: nowDate.getFullYear(),
                month: nowDate.getMonth() + 1,
                date: nowDate.getDate()+2,
            }
            const newmonth = date.month>9?date.month:'0'+date.month
            const day = date.date>9?date.date:'0'+date.date
            this.updateTime = date.year + '-' + newmonth + '-' + day
                }
                else if(flag=="3"){
                  const nowDate = new Date();
            const date = {
                year: nowDate.getFullYear(),
                month: nowDate.getMonth() + 1,
                date: nowDate.getDate()+3,
            }
            const newmonth = date.month>9?date.month:'0'+date.month
            const day = date.date>9?date.date:'0'+date.date
            this.updateTime = date.year + '-' + newmonth + '-' + day
                }
        
            this.showConferences()
          
                //强制刷新
                this.$forceUpdate()
},

    Changedname(flag1){
              this.name2=flag1
                
        //this.$http.get('http://127.0.0.1:8000/form/yy_conference?conference_id=' + value)
        //.then((response) => {
          //var res = JSON.parse(response.bodyText)
          //if (res.error_num === 0) {
            //this.showConferences()
          //} else {
            //this.$message.error('后端没传')
            //console.log(res['msg'])
          //}
        //})
                //强制刷新
                this.$forceUpdate()
},
    qingkong(){
      this.value11=''
      this.name2 =''
    },
    draw(){
      this.$http.get('http://127.0.0.1:8000/form/draw_forms')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
  
            this.formslist = res
            console.log(this.formslist)

        })
    },
    bookway(id,time,stutes){
      if(stutes==0)
        return "正在维修"
      for (var i=0;i<this.formslist[0].length;i++){
            if(this.formslist[0][i]==id &&this.formslist[1][i]==time&&this.formslist[2][i]==this.updateTime)
                return  "已预约"
    }
    return '未预约'
    },
    way(id,time,stutes){
      if(stutes==0)
        return "info"
      for (var i=0;i<this.formslist[0].length;i++){
            if(this.formslist[0][i]==id &&this.formslist[1][i]==time&&this.formslist[2][i]==this.updateTime)
                return  "danger"
      }
      return 'success'
    },

    way1(PPG1){
      if(PPG1== "已预约" ){
        return "el-icon-turn-off"
      }
      else{
        return "el-icon-open"
      }
    },
  mounted() {
    let _this = this; // 声明一个变量指向Vue实例this，保证作用域一致
    this.timer = setInterval(() => {
      _this.date = new Date(); // 修改数据date
    }, 1000)
  },

  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer); // 在Vue实例销毁前，清除我们的定时器
    }
  },
    nextDate(){
      const nowDate = new Date();
            const date = {
                year: nowDate.getFullYear(),
                month: nowDate.getMonth() + 1,
                date: nowDate.getDate() + 1,
            }
            const newmonth = date.month>10?date.month:'0'+date.month
            const day = date.date>10?date.date:'0'+date.date
            this.updateTime = date.year + '-' + newmonth + '-' + day
      this.$http.get('http://127.0.0.1:8000/form/show_conference?conference_id=' + this.updateTime)//已经作废
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.conferenceList = res['list']
          } else {
            this.$message.error('…………')
            //console.log(res['msg'])
          }
        })
    },

    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
<style scoped>
.mask {
  background-color: #000;
  opacity: 0.3;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1
}
.pop {
  background-color: #fff;
 
  position: fixed;
  top: 100px;
  left: 300px;
  width: calc(100% - 600px);
  height:calc(100% - 200px);
  z-index: 2
}
.btn {
  background-color: #fff;
  border-radius: 4px;
  border: 1px solid blue;
  padding: 4px 12px;
}
</style>