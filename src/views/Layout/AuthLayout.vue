<template>
  <v-app id="inspire" :class="{'dark-theme': darkTheme}">
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="px-0 fill-height">
        <v-row>
        <v-avatar
          class="mr-10"
          color="grey darken-1"
          size="40"
        ></v-avatar>

        <v-btn
          v-for="link in links"
          :key="link"
          :to="link.path"
          text
          class="font-weight-bold"

        >
          {{ link.name }}
        </v-btn>
        <v-spacer></v-spacer>
        <v-responsive max-width="260">
          <text-field label="Search" color="primary" prepend-inner-icon="mdi-magnify"/>
        </v-responsive>
        <btn-comp @click="toggleTheme" BtnLabel="Mode" style="margin-right: 10px;" ></btn-comp>
      </v-row>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item
                  v-for="navLink in navLinks"
                  :key="navLink"
                  :to="navLink.path"
                  text
                  link
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ navLink.name }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item
                  link
                  color="grey lighten-4"
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      Logout
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>
          <v-col>
            <v-sheet min-height="100vh" rounded="lg">
              <v-row>
                <v-col cols="12" md="8">
                  <v-img max-height="150" max-width="400" src="../../assets/Img/Pie.png"/>
                  <v-row style="margin-top: 20px;">
                    <v-col cols="6" md="2">
                      <Btn-dia BtnLabel="Turn On" title="Turn off " icon="mdi-watering-can" text="Successfully Turn On Valve !"/>
                    </v-col>
                    <v-col cols="6" md="2">
                      <Btn-dia BtnLabel="Turn Off" title="Turn on valve !" icon="mdi-emoticon" text="Successfully Turn Off Valve !"/>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col cols="12" md="4">
                  <weather-card />
                </v-col>
              </v-row>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import WeatherCard from '../../components/WeatherCard.vue'
import BtnComp from '../../components/BtnComp.vue'
import BtnDia from '../../components/DialogVue.vue'
import TextField from '../../components/TextField.vue'

  export default {
  components: { 
    WeatherCard,
    BtnDia,
    TextField,
    BtnComp
  },
    name: 'AuthLayout',
    component: {
      WeatherCard,
      BtnComp,
      BtnDia,
      TextField
    },
    data: () => ({
      links: [
        // 'Dashboard',
        // 'Parameter Setting',
        // 'History',
        {
          name: 'Dashboard', path: '/home'
        },
        {
          name: 'Parameter Setting', path:'/setting'
        },
        {
          name: 'History', path: '/history'
        }
      ],
      navLinks : [
        {
          name: 'Notification', path: ''
        },
        {
          name: 'Report', path: ''
        },
        {
          name: 'Setting', path: ''
        },

      ],
      darkTheme: false,
    }),
    methods: {
    toggleTheme() {
      this.darkTheme = !this.darkTheme;
      this.$vuetify.theme.dark = this.darkTheme;
    },
  },
  }
</script>
<style>

.dark-theme {
  background-color: #1e1e1e; 
  color: white; 
}


.dark-theme .v-main, .dark-theme .v-app-bar, .dark-theme .v-card {
  background-color: transparent;
  color: white; 
}


.dark-theme .v-btn, .dark-theme .v-btn--text, .dark-theme .v-list-item {
  color: white;
}

</style>