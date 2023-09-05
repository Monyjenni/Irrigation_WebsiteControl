<template>
  <v-btn
  v-bind="$attrs"
  v-on="$listeners"
  rounded
  dense
  >
  <slot name="icon"></slot>
    {{ BtnLabel }}
</v-btn>
</template>

<script>
  export default {
    name: 'BtnComp',
    props: {
      BtnLabel : {
        type: String,
        required: true
      },
      BtnColor: {
        type : String,
        required: true
      },
      icon: {
        type: String
      }
    }
    
  }
</script>

<style scoped>

</style>