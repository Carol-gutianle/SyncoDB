<style scoped>
.el-table .cell{
  white-space: pre-wrap;
}
</style>
<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">
      <el-card style="width: 40%; margin: 10px">

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="show()">显示本地所有数据库名字</el-button>
        </div>
        <div style="margin: 50px;"></div>
        <el-table
          :data="dbData"
          border
          stripe
          style="width: 100%">
          <el-table-column
            fixed
            prop="id"
            label="id"
            width="100">
          </el-table-column>
          <el-table-column
            fixed
            prop="fileName"
            label="fileName"
            width="490">
          </el-table-column>
        </el-table>

      </el-card>

      <el-card style="width: 40%; margin: 10px">

        <p>执行SQL</p>
        <div style="margin: 20px;"></div>

        <el-form :label-position="labelP" model="sqlform"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <el-form-item label="dbname" :label-width="formLabelWidth" >
            <el-input style="width: 350px"
                      placeholder="请输入数据库名"
                      v-model="sqlform.dbname"
                      clearable>
            </el-input>

          </el-form-item>

          <el-form-item label="sqlQuery" :label-width="formLabelWidth" >
            <el-input style="width: 350px"
                      placeholder="请输入sql"
                      v-model="sqlform.sqlQuery"
                      clearable>
            </el-input>
          </el-form-item>


        </el-form>
        <div style="margin: 30px;"></div>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="submit('sqlform')">运行</el-button>
        </div>

      </el-card>



      <!--这里应该是对着后端的数据改成适合的-->
      <el-card style="width: 40%; margin: 10px">

        <p>运行结果查看</p>
        <el-table
          :data="tableData"
          border
          stripe
          style="width: 100%">
          <el-table-column
            fixed
            prop="操作"
            label="操作"
            width="590">
          </el-table-column>

        </el-table>
        <div style="margin: 30px;"></div>
        <el-table
          :data="tableData1"
          border
          stripe
          style="width: 100%">

          <el-table-column
            fixed
            prop="运行结果"
            label="运行结果"
            width="590">
          </el-table-column>
        </el-table>
        <div style="margin: 30px;"></div>
      </el-card>
    </div>
  </div>
</template>

<script>
import request from "../util/request";

var check1 = (rule, value, callback) => {
  if (!value) {
    return callback(new Error('不能为空'));
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
      labelP:'top',
      sqlform:{
        dbname: '',
        sqlQuery: '',
      },

      tableData: [],
      tableData1: [],
      dbData: [],
      rules:{
        rule1:[ { validator: check1, trigger: 'blur'  } ]
      }
    };
  },


  methods: {
    //输入sql指令
    submit(sqlform) {
      request.post("api/sqlExecute/",this.sqlform).then(res=>{
        // this.$message({
        //   message: res.data.status
        //
        // })
        this.tableData=res.data.res1
        this.tableData1=res.data.res2
      })
    },
    show() {
      request.post("api/getDatabase/").then(res=>{
        this.dbData=res.data.datas
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


