<template>
  <div class="home">

    <el-row display="margin-top:10px">
      <el-input v-model="input_user_id" placeholder="请输入搜索用户编号"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="showUsers()" style="float:left; margin: 2px;">搜索</el-button>
    </el-row>

    <el-row>
      <el-table :data="userList" style="width: 100%" border>
        <el-table-column prop="room" label="会议室编号" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.room }}</template>
        </el-table-column>
          <el-table-column prop="user_id" label="申请人编号" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.user_id }}</template>
        </el-table-column>
          <el-table-column prop="data" label="申请日期" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.data }}</template>
        </el-table-column>
        <el-table-column prop="service" label="任务类别" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.service }}</template>
        </el-table-column>
          <el-table-column prop="equip" label="具体内容" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.equip }}</template>
        </el-table-column>
        <el-table-column prop="state" label="任务状态" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.state }}</template>
        </el-table-column>
        <el-table-column label="操作" min-width="100">
          <template slot-scope="scope"><!--作用域插槽-->
            <el-button type="primary" icon="el-icon-check" size="mini" @click="editUsers(scope.row.pk)"></el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        addUserVisible: false,
        editUserVisible: false,
        input_user_id: '',
        delete_User_id: '',
        addForm: {},
        editForm: {},
        userList: [],
      }

    },
    mounted: function () {
      this.showUsers()
    },
    methods: {
      showUsers () {
        this.$http.get('http://127.0.0.1:8000/hq/show_baoxiu?user_id=' + this.input_user_id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              this.userList = res['list']
            } else {
              this.$message.error('查询报修失败')
              console.log(res['msg'])
            }
          })
      },
      editUsers (id) {
        this.$http.get('http://127.0.0.1:8000/hq/edit_baoxiu?user_id=' + id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num == 0) {
              this.$message.success('任务完成')
              this.showUsers()
             }
             else{
             this.$message.error(res.msg)
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