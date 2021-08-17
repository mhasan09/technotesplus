<template>
<Nav/>
  <router-view/>
</template>
<script>
import { watch } from '@vue/runtime-core'
import Nav from './components/Nav.vue'
import { useRoute } from 'vue-router';
export default{
  components:{
    Nav
  },
  setup() {
    const route = useRoute();
  }


}
</script>

<style>
</style>
