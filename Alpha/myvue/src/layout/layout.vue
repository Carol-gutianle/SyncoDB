<template>
  <div >
    <myhead />
    <div style="display: flex">
      <mymenu/>
      <router-view style="flex: 1"/>

    </div>
  </div>
</template>

<style>

</style>
<script>


import myhead from "../components/myhead";
import mymenu from "../components/mymenu";


export default {
  name: "layout",
  components:{
    myhead,
    mymenu
  }
}
</script>

