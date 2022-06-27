<template>
  <div>
    <div style="height: 40px">
    </div>

    <el-table
      :data="tableData"
      border
      stripe
      style="width: 100%">
      <el-table-column
        fixed
        prop="username"
        label="username"
        width="100">
      </el-table-column>
      <el-table-column
        prop="name"
        label="name"
        width="100">
      </el-table-column>
      <el-table-column
        prop="age"
        label="age"
        width="100">
      </el-table-column>
      <el-table-column
        prop="teleno"
        label="teleno"
        width="100">
      </el-table-column>

      <el-table-column

        label="操作"
        width="100">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" >更改</el-button>
          <el-popconfirm
            title="确定删除吗？"
            @confirm="handleDelete(scope.row.username)">
            <el-button type="text" slot="reference">删除</el-button>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>

    <div style="margin: 10px 0">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[5, 10, 15, 20]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total">
      </el-pagination>
    </div>

    <el-dialog title="输入更改信息" :visible.sync="dialogFormVisible2" width="30%">
      <el-form :model="form" label-width="100px">
        <el-form-item label="username" :label-width="formLabelWidth">
          <el-input

            placeholder="请输入内容"
            v-model="form.username"
            :disabled="true"
            clearable>
          </el-input
          >
        </el-form-item>
        <el-form-item label="name" :label-width="formLabelWidth">
          <el-input

            placeholder="请输入内容"
            v-model="form.name"
            clearable>
          </el-input>
        </el-form-item>
        <el-form-item label="age" :label-width="formLabelWidth">
          <el-input

            placeholder="请输入数字"
            v-model="form.age"
            clearable>
          </el-input>
        </el-form-item>
        <el-form-item label="teleno" :label-width="formLabelWidth">
          <el-input

            placeholder="请输入内容"
            v-model="form.teleno"
            maxlength="11"
            show-word-limit
            clearable>
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible2 = false">取 消</el-button>
        <el-button type="primary" @click="save2(form)">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</template>

<script>
import request from "../util/request";

export default {
  name: "home",
  data() {
    return {
      form:{},
      dialogFormVisible:false,
      dialogFormVisible2:false,
      search: '',
      currentPage4:1,
      pageSize:10,
      total:5,
      tableData: []

    }
  },
  created() {
    this.load()
  },
  methods:{
    load(){
      request.get("/api/person/getPage",{
        params:{
          pageNum:this.currentPage4,
          pageSize:this.pageSize,
          search:this.search
        }
      }).then(res=>{
        console.log(res.data)
        this.tableData=res.data.list
        this.total = res.data.total
        this.pageSize = res.data.pageSize
      })
    },
    save2(formName){

      request.put("/api/person/updatePerson",this.form).then(res=>{
        console.log(res) //打印出来
        if(res.code!=='0'){
          this.$message({
            type:"success",
            message:"更新成功"
          })
        }else{
          this.$message({
            type:"error",
            message:"更新失败"
          })
        }
        this.load()
        this.dialogFormVisible2=false
      })


    },
    handleDelete(username){
      console.log(username)
      request.delete("/api/person/deletePerson/"+username).then(res=>{
        if(res.code!=='0'){
          this.$message({
            type:"success",
            message:"删除成功"
          })
        }else{
          this.$message({
            type:"error",
            message:res.msg
          })
        }
        this.load()

      })
    },
    handleClick(row){
      // this.form.username=row.username
      // this.form.name = row.name;
      // this.form.age = row.age;
      // this.form.teleno = row.teleno;
      this.form=JSON.parse(JSON.stringify(row))
      this.dialogFormVisible2=true
    },
    handleCurrentChange(pageNum){
      // 改变当前页触发函数
      this.currentPage4 = pageNum
      this.load()
    },
    handleSizeChange(pageSize){

      this.pageSize = pageSize
      this.load()
    }
  }
}

</script>

<style scoped>

</style>
