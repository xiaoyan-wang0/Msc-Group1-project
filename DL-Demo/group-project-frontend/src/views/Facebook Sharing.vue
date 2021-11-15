<template>
 
<div class="fb-share-button" 
data-href="https://alexey-avdeev.com/vanilla-sharing/" 
data-layout="button_count">
</div>

 
<a href="javascript:window.open('http://www.facebook.com/sharer.php?u='+encodeURIComponent('https://alexey-avdeev.com/vanilla-sharing/')+'&title=' +encodeURIComponent('HALLO'))" style="font-size: 14px; margin-right: 50px">
      分享Facebook
</a>

</template>






<script>


(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));



</script>




