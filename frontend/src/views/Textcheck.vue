<template>

  <div class="home">
    <h1 class="title">检查工具</h1>

    <el-row display="margin-top:10px">
      <el-input v-model="input_text" placeholder="请输入文本内容"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="textSubmit()" style="float:left; margin: 2px;">点击查询</el-button>
    </el-row>

    <el-row>
      <el-table :data="tableData" style="width: 100%" border>
        <el-table-column label="输入的文本" min-width="100">
          <template v-slot:default="scope">
            <span v-html="scope.row.before_text"></span>
          </template>
        </el-table-column>

        <el-table-column label="检查的结果" min-width="100">
          <template v-slot:default="scope">
            <span v-html="scope.row.after_text"></span>
          </template>
        </el-table-column>

      </el-table>
    </el-row>

  </div>

</template>


<script>

export default {
  name: 'home',
  computed: {
  },
  data() {
    return {
      input_text: '',
      data: {},
      before_text: '',
      after_text: '',
      tableData: []
    }
  },
  mounted: function () {
  },

  methods: {

    textSubmit() {
      if (this.input_text === '') {
        this.$message.warning("输入不能为空");
      } else {
        this.$http.get('http://127.0.0.1:9999/text_check/' + '?input_text=' + this.input_text)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.result === 0) {
              this.data = res['data']
              this.before_text = this.data['before_text']
              this.after_text = this.data['after_text']

              var check_list = this.data['check_list']

              for (var i = 0; i < check_list.length; i++) {
                var correct_frag = check_list[i]['correct_frag'];
                var ori_frag = check_list[i]['ori_frag'];
                this.before_text = this.before_text.replaceAll(ori_frag, '<span style="color: red; font-weight: bolder">' + ori_frag + '</span>')
                this.after_text = this.after_text.replaceAll(correct_frag, '<span style="color: green; font-weight: bolder">' + correct_frag + '</span>')
              }

              this.tableData = []
              this.tableData.push({before_text: this.before_text, after_text: this.after_text})
            } else {
              this.$message.error('查询失败')
              console.log(res['msg'])
            }
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


