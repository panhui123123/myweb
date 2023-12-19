<template>

  <div class="home">
    <h1 class="title">用户管理</h1>

    <el-row display="margin-top:10px">
      <el-input v-model="name" placeholder="请输入姓名"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-input v-model="phone" placeholder="请输入号码"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="addUser()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row display="margin-top:10px">
      <el-input v-model="searchName" placeholder="请输入姓名"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="searchUser()" style="float:left; margin: 2px;">搜索</el-button>
    </el-row>
    <el-row>
      <el-table :data="data" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template v-slot:default="scope"> {{ scope.row.id }}</template>
        </el-table-column>
        <el-table-column prop="name" label="姓名" min-width="100">
          <template v-slot:default="scope"> {{ scope.row.name }}</template>
        </el-table-column>
        <el-table-column prop="phone" label="电话" min-width="100">
          <template v-slot:default="scope"> {{ scope.row.phone }}</template>
        </el-table-column>
        <el-table-column label="操作" min-width="100">
          <template v-slot:default="scope">
            <el-button type="primary" @click="editUser(scope.row)" style="margin: 2px;">编辑</el-button>
            <el-button type="danger" @click="deleteUser(scope.row)" style="margin: 2px;">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5, 10, 20, 50]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        style="margin-top: 10px">
      </el-pagination>


    </el-row>

    <el-dialog title="编辑用户" :visible.sync="dialogVisible" width="30%" @close="resetForm">
      <el-form :model="editForm">
        <el-form-item label="姓名">
          <el-input v-model="editForm.name"></el-input>
        </el-form-item>
        <el-form-item label="电话">
          <el-input v-model="editForm.phone"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitEdit()">确 定</el-button>
      </div>
    </el-dialog>

  </div>

</template>


<script>
import {MessageBox} from "element-ui";

export default {
  name: 'home',
  data() {
    return {
      name: '',
      phone: '',
      searchName: '',
      data: [],
      dialogVisible: false,
      editForm: {
        id: '',
        name: '',
        phone: ''
      },
      total: 0,
      pageSize: 10,
      currentPage: 1,
    }
  },
  mounted: function () {
    this.showUser()
  },
  methods: {
    addUser() {
      if (this.phone === "" || this.name === "") {
        this.$message.warning("name or phone can not be blank")
      } else {
        this.$http.post('http://127.0.0.1:9999/user_add/',
          {
            name: this.name, phone: this.phone
          },
          {
            headers: {'Content-Type': 'application/json'}
          }
        )
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.result === 0) {
              this.showUser()
              this.$message.success(res.msg)
            } else {
              this.$message.error(res.msg)
              console.log(res['msg'])
            }
          })
      }
    },

    showUser(page = this.currentPage) {
      this.$http.get('http://127.0.0.1:9999/user_list/?page=' + page + '&pageSize=' + this.pageSize)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.result === 0) {
            this.data = res['data']
            this.total = res['total']
          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
        })
    },

    searchUser(page = this.currentPage) {
      this.$http.get('http://127.0.0.1:9999/user_list/?name=' + this.searchName + '&page=' + page + '&pageSize=' + this.pageSize)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.result === 0) {
            this.data = res['data']
            this.total = res['total']
            this.$message.success("查询成功")
          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
        })
    },

    deleteUser(user) {
      MessageBox.confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$http.post('http://127.0.0.1:9999/user_delete/', {id: user.id}, {
          headers: {'Content-Type': 'application/json'}
        }).then((response) => {
          if (response.status === 500) {
            this.$message.error('服务器错误')
          }
          var res = JSON.parse(response.bodyText)
          if (res.result === 0) {
            this.showUser()
            this.$message.success(res.msg)
          } else {
            this.$message.error(res.msg)
            console.log(res['msg'])
          }
        })
      }).catch(() => {
        this.$message.info('已取消删除')
      });
    },

    editUser(user) {
      this.dialogVisible = true;
      console.log(this.dialogVisible);
      this.editForm = Object.assign({}, user);
      console.log(this.editForm);

    },

    submitEdit() {
      this.$http.post('http://127.0.0.1:9999/user_edit/', this.editForm, {
        headers: {'Content-Type': 'application/json'}
      }).then((response) => {
        if (response.status === 500) {
          this.$message.error('服务器错误')
        }
        var res = JSON.parse(response.bodyText)
        if (res.result === 0) {
          this.showUser()
          this.$message.success(res.msg)
          this.dialogVisible = false;
        } else {
          this.$message.error(res.msg)
          console.log(res['msg'])
        }
      })
    },

    resetForm() {
      this.editForm = {
        id: '',
        name: '',
        phone: ''
      };
    },

     handleSizeChange(val) {
      this.pageSize = val;
      this.showUser();
    },

    handleCurrentChange(val) {
      this.currentPage = val;
      this.showUser();
    },

  }
}
</script>


<style scoped>
.title {
  font-size: 2em;
  color: #333;
  margin-bottom: 20px;
}

.home {
  padding: 20px;
  box-sizing: border-box;
  margin-left: 300px;
}

.el-row {
  margin-bottom: 20px;
}

.el-input {
  margin-right: 10px;
}

.el-button {
  margin-right: 10px;
}

.el-table {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.el-dialog {
  top: 20vh;
}

.dialog-footer {
  text-align: right;
}

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


