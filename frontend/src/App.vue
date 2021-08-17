<template>
<Nav/>
  <router-view/>
</template>
<script>
import { watch } from '@vue/runtime-core'
import Nav from './components/Nav.vue'
export default{
  components:{
    Nav
  },


}
</script>

<style>
</style>
