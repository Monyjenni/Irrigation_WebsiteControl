<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
      rounded
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
          rounded
          dense
        >
        {{ BtnLabel }}
        </v-btn>
      </template>

      <v-card>
        <v-col cols="12">
          <v-card-title class="text-h5 grey lighten-2">
          {{ title }}
        </v-card-title>
        <v-icon color="green darken-2"> {{icon}}</v-icon>
        <v-card-text>
        {{ text }}
        </v-card-text>
      </v-col>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
  export default {
    name: 'BtnDia',
    data () {
      return {
        dialog: false,
      }
    },
    props: {
      BtnLabel : {
        type: String,
        required: true
      },
      BtnColor: {
        type : String,
        required: true
      },
      title: {
        type: String
      },
      icon: {
        type: String
      },
      text: {
        type: String,
        required: true
      }
    }
  }
</script>