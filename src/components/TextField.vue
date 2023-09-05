<template>
  <v-text-field
  v-bind="$attrs"
  v-on="$listeners"
  dense
  rounded
  outline
  :label="label"
  :color="color"
  filled
  />
</template>

<script>
  export default {
    name: 'TextFieldComp',
    props: {
      label: {
        type: String,
        required: true
      },
      color: {
        type: String,
        required: true
      },
    }
    
  }
</script>

<style scoped>

</style>