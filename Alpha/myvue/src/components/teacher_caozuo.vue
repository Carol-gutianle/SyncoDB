<template>
  <div >
    <div style="height: 40px">
    </div>
    <div style="text-align: center;width: 100%; padding-left: 400px;margin: auto">



      <el-card style="width: 40%; margin: 10px">

        <i class="el-icon-lock"></i>
        <p>输入数据库指令</p>

        <el-form :model="form"  class="demo-ruleForm" label-position="left" label-width="80px"  status-icon :rules="rules" ref="form">

          <el-form-item label="mysql" :label-width="formLabelWidth" prop="tpass">
            <el-input style="width: 200px"
                      placeholder="请输入mysql指令"
                      v-model="form.tpass"
                      clearable>
            </el-input>
          </el-form-item>

          <div style="margin: 50px;"></div>
        </el-form>

        <div style="text-align: center">
          <el-button type="primary" icon="el-icon-edit" @click="gocaozuo2">运行</el-button>
        </div>

      </el-card>
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

export default {
  name: "teacher_caozuo",
  data() {
    return {
      form:{
        kno:'',
        tpass:'',
      },
      search: '',
    };
  },

  methods: {
    save(form) {
      this.$refs[form].validate((valid) => {
        if (valid) {

          request.post("/api/person/addPerson", this.form).then(res => {

            console.log(res.data); //打印出来
            if ((res.data !== 0)) {
              if ((res.data === 1)){
                this.$message({
                  type: "success",
                  message: "成功添加"+this.form.name
                })
              }else{
                this.$confirm("用户名"+this.form.username+"已存在，需要修改信息吗？", '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                }).then(() => {
                  request.put("/api/person/updatePerson",this.form).then(res=> {
                    console.log(res) //打印出来
                    if (res.code !== '0') {
                      this.$message({
                        type: "success",
                        message: "修改成功"
                      })

                    }
                  });

                }).catch(() => {
                  this.$message({
                    type: 'info',
                    message: '已取消修改'
                  });
                });
              }

            } else {
              this.$message({
                type: "error",
                message: "名称"+this.form.name+"重复,请重新填写"
              })
            }
          })
        }
      });
    },
  }

}
</script>

<style scoped>

</style>
