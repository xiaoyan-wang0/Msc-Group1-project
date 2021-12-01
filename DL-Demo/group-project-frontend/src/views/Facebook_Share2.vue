<template>
 <div id="fb-root">
<div class="fb-share-button" 
data-href="https://alexey-avdeev.com/vanilla-sharing/" 
data-layout="button_count">
</div>
</div>


 
<a href="javascript:window.open('http://www.facebook.com/sharer.php?u='+encodeURIComponent('https://alexey-avdeev.com/vanilla-sharing/')+'&title=' +encodeURIComponent('HALLO'))" style="font-size: 14px; margin-right: 50px">
      分享Facebook
</a>


<a href="javascript:window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent('https://alexey-avdeev.com/vanilla-sharing/')+'&title=' +encodeURIComponent('HALLO'))" style="font-size: 14px; margin-right: 50px">
      分享T
</a>
<!-- 
https://www.facebook.com/dialog/share?
  app_id=145634995501895
  &display=popup
  &href=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2F
  &redirect_uri=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer -->



</template>






<script>


(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

 window.fbAsyncInit = function () {
        var appId = '612741260170399';
        FB.init({
            appId: appId,
            xfbml: true,
            version: 'v2.9'
        });
    };

    // FB Share with custom OG data.
    (function($) {

        $('.fb_share_btn').on('click', function (event) {
            event.preventDefault();
            event.stopImmediatePropagation();

                // Dynamically gather and set the FB share data. 
                var FBDesc      = 'Your custom description';
                var FBTitle     = 'Your custom title';
                var FBLink      = 'http://example.com/your-page-link';
                var FBPic       = 'http://example.com/img/your-custom-image.jpg';

                // Open FB share popup
                FB.ui({
                    method: 'share_open_graph',
                    action_type: 'og.shares',
                    action_properties: JSON.stringify({
                        object: {
                            'og:url': FBLink,
                            'og:title': FBTitle,
                            'og:description': FBDesc,
                            'og:image': FBPic
                        }
                    })
                },
                function (response) {
                // Action after response
                })
        })

    })( jQuery );

</script>




