<template>
  <v-app id="inspire">
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height">
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
        <v-row class="ml-auto">
            <v-responsive max-width="260">
            <text-field label="Search" color="primary" prepend-inner-icon="mdi-magnify"/>
          </v-responsive>
          <btn-comp @click="toggleTheme" BtnLabel="Mode" />
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
                <v-col cols="12">
                  <v-img max-height="150"
                  max-width="250" 
                  src="../../assets/Img/Pie.png"/>
                </v-col>
                <Btn-dia BtnLabel="Turn On" title="Turn off " icon="mdi-watering-can" text="Successfully Turn On Valve !"/>
                <Btn-dia BtnLabel="Turn Off" title="Turn on valve !" icon="mdi-emoticon" text="Successfully Turn Off Valve !"/>
              </v-row>
              <v-col cols="12">
                <weather-card />
              </v-col>
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
      darkTheme: true,
    }),
    methods: {
    toggleTheme() {
      this.darkTheme = !this.darkTheme;
      this.$vuetify.theme.dark = this.darkTheme;
    },
  },
  }
</script>