<template>

<div class="home">
<el-row display="margin-top:10px">
<!--el-input v-model="input" placeholder="请输入会议室编号" style="display:inline-table; width: 30%; float:left"></el-input>
<el-button type="primary" @click="addConference()" style="float:left; margin: 2px;">新增</el-button-->
<el-input v-model="input_conference_id" placeholder="请输入搜索会议室编号" style="display:inline-table; width: 30%; float:left"></el-input>
<el-button type="primary" @click="showForms()" style="float:left; margin: 2px;">搜索</el-button>

</el-row>
<el-row>
<el-table :data="partlist" style="width: 1000%" border>
  <el-table-column prop="conference_id" label="预约人用户编号" min-width="100">
  <template slot-scope="scope"> {{ scope.row.fields.user_id }} </template>
  </el-table-column>

  <el-table-column prop="conference_capacity" label="会议室编号" min-width="100">
  <template slot-scope="scope"> {{ scope.row.fields.room }} </template>
  </el-table-column>

  <el-table-column prop="conference_capacity" label="会议时间" min-width="100">
  <template slot-scope="scope"> {{ scope.row.fields.day}} </template>
  </el-table-column>

  <el-table-column prop="Conference_status" label="会议时段" min-width="100">
    <template slot-scope="scope"> {{ scope.row.fields.time_id == 1 ? '1:00 - 2:00' : scope.row.fields.time_id == 2 ? '2:00 - 3:00': scope.row.fields.time_id == 3 ? '3:00 - 4:00' : scope.row.fields.time_id == 4 ? '10:00 - 11:00': scope.row.fields.time_id == 5 ? '11:00 - 12:00':''}} </template>
  </el-table-column> 
  <el-table-column prop="Conference_status" label="参会人员" min-width="100">
    <template slot-scope="scope"> {{ scope.row.fields.Participants}} </template>
  </el-table-column> 
  <el-table-column prop="Conference_status" label="状态" min-width="100">
    <template slot-scope="scope"> {{ scope.row.fields.statu}} </template>
  </el-table-column> 
   <el-table-column prop="conference_authorization" label="取消预约" min-width="100">
<template slot-scope="scope">
<div id="app">
<el-switch
  v-model= "scope.row.fields.statu"
  :disabled= "way(user_id,scope.row.fields.user_id,scope.row.fields.statu)"
  active-color="#ff4949"
  inactive-color="#13ce66"
  active-value = "已取消"
  inactive-value = "已预约"
   @change="open(scope.row.pk)">
</el-switch>
      </div>
    </template>
</el-table-column> 

</el-table>
  </el-row>


        <el-dialog
                title="取消预约"
                :visible.sync="ORZ"
                width="40%"
                @close="hy">

            <span slot="footer" class="dialog-footer">
                <el-button @click="hy">取 消</el-button>
                <el-button type="primary" @click="cancelbook(trans_id)">确 定</el-button>
            </span>
        </el-dialog>


  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      ORZ: false,
      value12: false,
      addConferenceVisible: false,
      addForm: {},
      date: new Date(),
      showModal: false,
      input: '',
      input_conference_id: '',
      now_conference_id: '',
      now_time: '',
      delete_conference_id: '',
      conferenceList: [],
      selected: '',    
      name1:[],
      name2:'',
      truename :[],
      show_time:'',
      name_draw:'',
      formslist:[],  
      partlist:[]   , 
      trans_id:'',
      user_id:'',
    }
  },

  mounted: function () {
    this.user_id = localStorage.user_id
    this.showForms()
    this.updateforms()
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
    deleteform(id){
      this.$http.get('http://127.0.0.1:8000/form/delete_form?id='+id)  //传的是会议室编号   
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
             this.$message.success('删除成功')
          } else {
            this.$message.error('删除失败')
          }
        })
        this.showForms()
    },
    way(homename,bookname,statu){
        if(homename==bookname & statu=='已预约')
          return false
        else
          return true
    },
    cancelbook(id1){
        this.$http.get('http://127.0.0.1:8000/form/cancel_book?id='+id1)  //传的是会议室编号   
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showForms()
            this.ORZ = false
             this.$message.success('取消预约成功')
          } else {
            this.$message.error('取消预约失败')
          }
        })
        

    },
    hy(){
      
        this.ORZ = false
        this.value12=false
         this.showForms()
    },
    updateforms(){
          this.$http.get('http://127.0.0.1:8000/form/update_forms')  //传的是会议室编号   
    },
    open(id) {
      this.ORZ = true
      this.trans_id=id
      },
    showForms () {
      this.$http.get('http://127.0.0.1:8000/form/participant?participant_id='+this.user_id+'&conference_id='+this.input_conference_id)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.partlist = res['list']
          } else {
            this.$message.error('查询表单失败')
          }
        })
    },
    
    draw(){
      this.$http.get('http://127.0.0.1:8000/form/draw_forms')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
            this.formslist = res
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
          }
        })
    },

    
  }
}
</script>


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