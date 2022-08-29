<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">

      <el-card style="width: 40%; margin: 10px">

        <i class="el-icon-lock"></i>
        <p>输入数据库指令</p>

        <el-form :model="uploadform"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <el-form-item label="mysql" :label-width="formLabelWidth" prop="sql">
            <el-input style="width: 200px"
                      placeholder="请输入mysql指令"
                      v-model="uploadform.sql"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="submit('uploadform')">运行</el-button>
        </div>

      </el-card>



      <!--这里应该是对着后端的数据改成适合的-->
      <el-card style="width: 40%; margin: 10px">
        <i class="el-icon-lock"></i>
        <p>运行结果查看</p>
        <el-table
          :data="tableData"
          border
          stripe
          style="width: 100%">
          <el-table-column
            fixed
            prop="题目号"
            label="题目号"
            width="240">
          </el-table-column>
          <el-table-column
            fixed
            prop="题目内容"
            label="题目内容"
            width="240">
          </el-table-column>
        </el-table>
      </el-card>
    </div>
  </div>
</template>

<script>
import request from "../util/request";

var checksql = (rule, value, callback) => {
  if (!value) {
    return callback(new Error('请输入mysql指令'));
  }
  else {callback();}
};

export default {
  created() {
    this.load()
  },

  data() {
    var cursql = this.$route.query.sql
    return {
      uploadform:{
        sql:cursql,
      },

      tableData: [],

      rules:{
        sql:[ { validator: checksql, trigger: 'blur'  } ]
      }
    };
  },


  methods: {
    //输入mysql指令
    submit(uploadform) {
      this.$refs[uploadform].validate((valid) => {
        var qs = require('querystring')
        console.log(valid)
        if(valid) {
          request.post("/zhixing",qs.stringify(this.uploadform)).then(res=>{
            this.$message({
              message: res.data.msg
            })
          })




        }
      })
    },

    //加载表格信息
    load(){
      request.get("/seleGData")
        .then(res=>{
          console.log(res.data.data)
          this.tableData=res.data.data
        })
    },

  }

}
</script>

<style scoped>

</style>
