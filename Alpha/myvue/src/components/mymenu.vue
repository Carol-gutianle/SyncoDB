<template>
  <div>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu   router default-active="path" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">

      <el-submenu index="1">

        <template slot="title">
          <i class="el-icon-edit"></i>
          <span slot="title">管理</span>
        </template>


        <el-menu-item-group>
          <el-menu-item index="teacher_denglu">数据库连接</el-menu-item>
        </el-menu-item-group>

        <el-menu-item-group>
          <el-menu-item index="teacher_caozuo">老师操作(之后改</el-menu-item>
        </el-menu-item-group>



      </el-submenu>


    </el-menu>
  </div>
</template>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 100vh;
}
</style>

<script>
export default {
  name: "mymenu",
  data() {
    return {
      isCollapse: true,
      path:this.$route.path
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style scoped>

</style>
