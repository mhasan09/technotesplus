<template>

  <transition name="modal-animation">
    <div class="modal" v-show="modalActive">
      <transition name="modal-animation-inner">
        <div class="modal-inner" v-show="modalActive">
        <i class="fa fa-times fa-lg" id="closeModalIcon" @click="close"></i>
          <p class="mb-6"></p>
          <slot />
          <p class="mt-4"></p>
        </div>
      </transition>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Modal',
  props: ["modalActive"],
  emits: ["closeModal"],
  setup(props, { emit }) {
    const close = () => {
      emit("closeModal");
    };
    return {
      close,
    };
  },
};
</script>

<style>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  position: fixed;
  top: 0;
  left: 0;
  background-color: #fff;
  border-radius: 1rem;
  
}
.modal-inner {
  position: relative;
  max-width: 640px;
  width: 80%;
  background-color: rgb(255, 255, 255);
  padding: 65px 16px;
}

.modal-background {
  z-index: 1000;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  background-color: rgba(0, 0, 0, 0.5);
}
#closeModalIcon{
  float: right;
  margin-right: 12%;
}
.modal-animation-enter-active,
.modal-animation-leave-active{
  transition: opacity .3s cubic-bezier(.52,.02,.19,1.02);
}
.modal-animation-enter-from,
.modal-animation-leave-to{
  opacity: 0;
}
.modal-animation-inner-enter-active{
  transition: all .3s cubic-bezier(.52,.02,.19,1.02) 0.15s;
}
.modal-animation-inner-leave-active{
  transition: all .3s cubic-bezier(.52,.02,.19,1.02);
}
.modal-animation-inner-enter-from{
  opacity: 0;
  transform: scale(0.8);
}
.modal-animation-inner-leave-to{
  transform: scale(0.8);
}

.modal-animation-leave-from{
  opacity: 1;
}


</style>