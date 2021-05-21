<template>
  <div class="home">

    <el-row display="margin-top:10px">
<!--      <el-input v-model="input_room" placeholder="请输入搜索会议室编号"-->
<!--                style="display:inline-table; width: 30%; float:left"></el-input>-->
<!--      <el-button type="primary" @click="showForms()" style="float:left; margin: 2px;">搜索</el-button>-->
    </el-row>

    <el-row>
      <el-table :data="formList" style="width: 100%" border>

        <el-table-column prop="room" label="会议室编号" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.room }}</template>
        </el-table-column>

        <el-table-column prop="day" label="日期" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.day }}</template>
        </el-table-column>

        <el-table-column prop="time_id" label="时间" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.time_id == 1 ? '1:00 - 2:00' : scope.row.fields.time_id == 2 ? '2:00 - 3:00': scope.row.fields.time_id == 3 ? '3:00 - 4:00' : scope.row.fields.time_id == 4 ? '10:00 - 11:00': scope.row.fields.time_id == 5 ? '11:00 - 12:00':''}}</template>
        </el-table-column>

        <el-table-column prop="Participants" label="参会人员" min-width="100">
<!--          <template slot-scope="scope"> {{ scope.row.fields.conference_authorization == 3 ? '高' : scope.row.fields.conference_authorization == 2 ? '中' : scope.row.fields.conference_authorization == 1 ? '低':'' }}</template>-->
          <template slot-scope="scope"> {{ scope.row.fields.Participants }}</template>
        </el-table-column>
          <el-table-column prop="Conference_status" label="状态" min-width="100">
        <template slot-scope="scope"> {{ scope.row.fields.statu}} </template>
         </el-table-column> 
        <el-table-column prop="conference_authorization" label="取消预约" min-width="100">
          <template slot-scope="scope" >
          <div id="app">
          <el-switch
            v-model= "scope.row.fields.statu"
            :disabled= "way(user_id,scope.row.fields.user_id,scope.row.fields.statu)"
            active-color="#ff4949"
            inactive-color="#13ce66"
            inactive-value="已预约"
            active-value ="已取消"
            @change="open(scope.row.pk)">
          </el-switch>
                </div>
              </template>
          </el-table-column> 
          <el-table-column label="操作" min-width="100">
          <template slot-scope="scope"><!--作用域插槽-->
            <el-button size="mini" type="danger" icon="el-icon-delete" @click="deleteform(scope.row.pk)"></el-button>
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
        trans_id:'',
        user_id: '',
        formList: []
      }
    },
    mounted: function () {
      this.user_id = localStorage.user_id

      this.showForms()
    },
    methods: {
    way(homename,bookname,statu){
        if(homename==bookname & statu=='已预约')
          return false
        else
          return true
    },
      hy(){
        this.ORZ = false
        this.value12=false
        this.showForms()
    },
    open(id) {
      this.ORZ = true
      this.trans_id=id
      },
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
      showForms () {
        this.$http.get('http://127.0.0.1:8000/api/show_forms?user_id=' + this.user_id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
 
            if (res.error_num === 0) {
              this.formList = res['list']
            } else {
              this.$message.error('查询预约失败')
 
            }
          })
      },
      deleteForm (delid) {

        this.$http.get('http://127.0.0.1:8000/api/delete_form?id=' + delid)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num === 0) {
              this.$message.success('删除预约成功')
              this.showForms()
            } else {
              this.$message.error('删除预约失败，请重试')

            }
          })
      }
    }
  }
</script>

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
