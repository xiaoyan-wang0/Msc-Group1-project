<template>
  <div class="hello">
    <button id='twitter' @click="login()" class="profile">twitter</button>
  </div>
</template>

<script>
import hello from 'hellojs/dist/hello.all.js'
export default {
  name: 'HelloWorld',
  mounted() {
    this.twws()


  },
  methods:{
      twws(){
        hello.init({
          twitter : 'SSwuT9iCWAekaGHaTTrv0YASA'
        },{
          scope : 'email',
          redirect_uri: 'http://localhost:5000/'
        });



      },
    login(){
      hello('twitter').login();
      // Listen to signin requests
      hello.on('auth.login', function(r) {
        // Get Profile
        hello( r.network ).api( '/me' ).then( function(p) {
          window.console.log(p)

        });
      });
    }
  }
}
</script>

