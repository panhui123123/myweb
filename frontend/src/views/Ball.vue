<template>

  <div class="home">
    <h1 class="title">双色球摇号</h1>

    <el-row display="margin-top:10px">
      <el-button type="primary" @click="generateLottery(1, [], [])" style="float:left; margin: 2px;">机选1注</el-button>
      <el-button type="primary" @click="generateLottery(5, [], [])" style="float:left; margin: 2px;">机选5注</el-button>
      <el-button type="primary" @click="generateLottery(10, [], [])" style="float:left; margin: 2px;">机选10注</el-button>

      <el-input
        placeholder="请输入注数"
        v-model="searchText"
        style="width: 100px; margin-left: 5px;">
      </el-input>

      <el-input
        placeholder="请输入红球杀号,以英文点分隔,如1.2.3"
        v-model="frontKill"
        style="width: 300px; margin-left: 5px;">
      </el-input>

      <el-input
        placeholder="请输入篮球杀号,以英文点分隔,如1.2.3"
        v-model="behindKill"
        style="width: 400px; margin-left: 5px;">
        <template #append>
      <el-button type="primary" @click="generateLottery(searchText, frontKill, behindKill)">生成</el-button>
    </template>
      </el-input>
    </el-row>

    <el-row>
      <el-table :data="tableData" style="width: 100%" border>
        <el-table-column label="注数" min-width="100">
          <template v-slot:default="scope"><span>{{ scope.$index + 1 }}</span></template>
        </el-table-column>

        <el-table-column label="红球结果" min-width="100">
          <template v-slot:default="scope">{{ scope.row.front_list }}</template>
        </el-table-column>

        <el-table-column label="篮球结果" min-width="100">
          <template v-slot:default="scope">{{ scope.row.behind_list }}</template>
        </el-table-column>
      </el-table>
    </el-row>

  </div>

</template>


<script>
import axios from "axios";

export default {
  name: 'home',
  computed: {
  },
  data() {
    return {
      tableData: [],
      searchText: "",
      frontKill: "",
      behindKill: ""
    }
  },
  mounted: function () {
  },

  methods: {
    generateLottery(num, front_kill, behind_kill) {
      if (num === "" || parseInt(num) > 100) {
          this.$message.error("请输入正整数且不要超过100")
      } else if (front_kill === "" || behind_kill === "") {
          this.$message.error("前区杀号和后区杀号必填")
      } else {
        axios.get('http://127.0.0.1:9999/ball/?num=' + num+ '&front_kill=' + front_kill + '&behind_kill=' + behind_kill)
        .then( (response) => {
            var res = response.data
            if (res.result === 1) {
              this.$message.error(res.msg);
            } else {
              this.tableData = res.data;
            }
          })
        .catch( (error) => {
          console.error(error)
          this.$message.error('请求失败，请检查网络连接或服务器状态')
          })
      }
    }
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



