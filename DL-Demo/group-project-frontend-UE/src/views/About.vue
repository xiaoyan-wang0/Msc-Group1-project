<template>
  <section class="blog-details spad">
        <div class="container">
            <div class="row d-flex justify-content-center">
                <div class="col-lg-8">
                    <div class="blog__details__title">
                        <h6>Last update date <span>- Nov 25th, 2021</span></h6>
                        <h2>For Authentic movie database(AMDB) Beginners: </h2>
                        <h2>Customised Multi-Sourced Movie Guide</h2>

                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="blog__details__pic">
                        <img src="img/blog/details/blog-details-pic.jpg" alt="">
                    </div>
                </div>
                <div class="col-lg-8">
                    <div class="blog__details__content">
                        <div class="blog__details__text">
                            <p>AMDb (Authentic Movie Database) is a movie review platform
                              with a movies recommender system and an authentic comment detector which could filter toxic
                              comments and analyze the sentiment of movie reviews. All the users can view or share some
                              related movie comments in a fair and authentic environment by using AMDb.</p>
                        </div>
                        <div class="blog__details__item__text">
                            <h4>Comment detector:</h4>
                            <img src="img/blog/details/bd-item-1.jpg" alt="">
                            <p>For AMDb, when users post their comment on AMDb platform, it will
                              be reminded this comment’s toxic rate and sentiment result to users.
                              Users can filter comments based on their tolerance for the toxic level or emotional bias.
                              In this way, a relatively non-toxic and fair communication environment can
                              be created for users.
                             <br/>
                              For other platforms, AMDb supports browsing of film reviews from TMDb, IMDb,
                              YouTube and Twitter. At the same time, each film review has been tested by the
                              toxic comment detector and its corresponding results are attached in the
                              end of the comment box.</p>
                        </div>
                        <div class="blog__details__item__text">
                            <h4>Toxic Level Icons and Explanation</h4>
                            <div class="t">
                              <img src="assets/toxic-green.png" alt="toxic level 1" width="10%" height="10%">
                            </div >
                            <div class="t">
                              <img src="assets/toxic-yellow.png" alt="toxic level 2" width="10%" height="10%">
                            </div>
                            <div class="t">
                              <img src="assets/toxic-red.png" alt="toxic level 3" width="10%" height="10%">
                            </div>
                            <div>
                              <p>When the toxic rate is within the range of 0-53%, the system will
                              use a green grunt head to indicate that it is non-toxic.
                              Green symbolizes non-toxicity.
                              When the toxic rate is within the range of 54-90%, the
                              system will use a yellow grunt to indicate that it is toxic.
                              When the toxic rate exceeds 90%, the red grunt head is used by
                              the system to indicate that it is sever toxic</p>
                            </div>
                        </div>
                        <div class="blog__details__item__text">
                            <h4>sentiment Level Icons and Explanation</h4>
                            <div class="t">
                              <img src="assets/sentiment-green.png" alt="Positive" width="10%" height="10%">
                            </div>
                            <div class="t">
                              <img src="assets/sentiment-red.png" alt="Negative" width="10%" height="10%">
                            </div>
                            <div>
                              <p>After the result of the detector detection, if
                              it is less than 50%, it is judged as negative by
                              the system and the red angry face icon is adopted;
                              if it is higher than 50%, it is regarded as positive
                              and the green smiling face icon is adopted.</p>
                            </div>
                        </div>

                        </div>
                    </div>
                </div>
            </div>
        </section>
</template>

<script>

</script>



<style lang="scss" scoped>

div .t{
  float:left;
	margin: 10px;
}

.blog-details {
	padding-top: 70px;
}


.spad {
	padding-top: 100px;
	padding-bottom: 100px;
}

.blog-details {
	padding-top: 70px;
}

.blog__details__title {
	text-align: center;
	margin-bottom: 70px;
}

.blog__details__title h6 {
	font-size: 15px;
	color: #ffffff;
	font-weight: 700;
	text-transform: uppercase;
	margin-bottom: 30px;
}

.blog__details__title h6 span {
	color: #b7b7b7;
	font-weight: 400;
	text-transform: none;
}

.blog__details__title h2 {
	color: #ffffff;
	font-size: 48px;
	font-weight: 700;
	line-height: 60px;
	margin-bottom: 38px;
}

.blog__details__title .blog__details__social a {
	display: inline-block;
	font-size: 15px;
	color: #ffffff;
	padding: 16px 35px 14px 20px;
	border-radius: 2px;
	margin-right: 6px;
}

.blog__details__title .blog__details__social a:last-child {
	margin-right: 0;
}

.blog__details__title .blog__details__social a.facebook {
	background: #3b5998;
}

.blog__details__title .blog__details__social a.pinterest {
	background: #ca2027;
}

.blog__details__title .blog__details__social a.linkedin {
	background: #0372b1;
}

.blog__details__title .blog__details__social a.twitter {
	background: #39a1f2;
}

.blog__details__title .blog__details__social a i {
	margin-right: 6px;
}


.blog__details__pic {
	margin-bottom: 30px;
}

.blog__details__pic img {
	min-width: 100%;
}


.blog__details__text {
	margin-bottom: 40px;
}

.blog__details__text p {
	color: #ffffff;
	font-size: 17px;
	line-height: 30px;
}

.blog__details__item__text {
	margin-bottom: 42px;
}

.blog__details__item__text h4 {
	color: #ffffff;
	font-weight: 700;
	margin-bottom: 35px;
}

.blog__details__item__text img {
	min-width: 100%;
	margin-bottom: 26px;
}

.blog__details__item__text p {
	color: #ffffff;
	font-size: 17px;
	line-height: 30px;
	margin-bottom: 0;
}
</style>