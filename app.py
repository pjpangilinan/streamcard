import streamlit as st
import streamlit.components.v1 as components

# idea & html/css code from
# https://codepen.io/Hyperplexed/pen/zYWdYoo

# adjusted for streamlit by TomJohn :-)

# ------------------------------------------------------------
#
#                  Visual settings and functions
#
# ------------------------------------------------------------

# ---------------- CSS ----------------

st.markdown("""
<style>
    .card-groups {
        /* background-color: rgb(0, 0, 0); */
        margin: 0px;
        height: 80vh;
        width: 100%;
        display: grid;
        place-items: center;
    
    }
    
    .card-groups,
    .card-group,
    .card {
        aspect-ratio: 5 / 7;
    }
    
    
    .card-group,
    .big-card {
        width: 30vmin;
    
    }
    
    .card-group {
        position: absolute;
        transition: transform 400ms ease;
    
    }
    
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        position: absolute;
        transition: transform 800ms cubic-bezier(.05, .43, .25, .95);
    
        background-position: center;
        background-size: cover;
    
    }
    
    .big-card {
        border-radius: 1vmin;
    
    }
    
    .little-card {
        width: 12vmin;
        border-radius: 2vmin;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        box-shadow: -1vmin 1vmin 2vmin rgba(0, 0, 0, 0.25);
    }
    
    .big-card:nth-child(2) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/image4.png");
        transform: translateX(-10%) rotate(-1deg);
    }
    
    .big-card:nth-child(4) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/image3.png");
        transform: rotate(2deg);
    }
    
    .big-card:nth-child(6) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/image2.png");
        transform: translateX(-6%) rotate(-3deg);
    }
    
    .big-card:nth-child(8) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/image1.png");
        background-size: contain;
        transform: translate(10%, 3%) rotate(5deg);
    }
    
    
    .little-card:nth-child(1) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/small1.jpg");
    }
    
    .little-card:nth-child(3) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/small2.jpg");
    }
    
    .little-card:nth-child(5) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/small3.jpg");
    }
    
    .little-card:nth-child(7) {
        background-image: url("https://raw.githubusercontent.com/TomJohnH/streamlit-cv/main/images/small4.jpg");
    }
    
    .card-group:hover>.card {
        box-shadow: -2vmin 2vmin 3vmin rgba(0, 0, 0, 0.4);
    }
    
    .card-group:hover>.big-card:nth-child(2) {
        transform: translate(-75%, 16%) rotate(-24deg);
    
    }
    
    .card-group:hover>.big-card:nth-child(4) {
        transform: translate(-25%, 8%) rotate(-8deg);
    }
    
    .card-group:hover>.big-card:nth-child(6) {
        transform: translate(25%, 8%) rotate(8deg);
    }
    
    .card-group:hover>.big-card:nth-child(8) {
        transform: translate(75%, 16%) rotate(24deg);
    }
    
    .card-group:hover>.little-card:nth-child(1) {
        transform: translate(200%, -160%) rotate(-15deg);
    }
    
    .card-group:hover>.little-card:nth-child(3) {
        transform: translate(160%, 170%) rotate(15deg);
    }
    
    .card-group:hover>.little-card:nth-child(5) {
        transform: translate(-200%, -170%) rotate(15deg);
    }
    
    .card-group:hover>.little-card:nth-child(7) {
        transform: translate(-280%, 140%) rotate(-15deg);
    }
    
    
    a.fill-div {
        display: block;
        height: 100%;
        width: 100%;
        text-decoration: none;
    }
</style>

# ------------------------------------------------------------
#
#                        front-end
#
# ------------------------------------------------------------

st.markdown("""<div class="card-groups">
    <div class="card-group" data-index="0" data-status="active">
        <div class="little-card card">
        </div>
        <div class="big-card card">
         <a id="link" href="https://discuss.streamlit.io/u/tomjohn/summary" class="fill-div"></a>
        </div>
        <div class="little-card card">
        </div>
        <div class="big-card card">
        <a id="link" href="https://stackoverflow.com/users/5627791/tomjohn" class="fill-div"></a>
        </div>
        <div class="little-card card">
        </div>
        <div class="big-card card">
        <a id="link" href="https://github.com/TomJohnH" class="fill-div"></a>
        </div>
        <div class="little-card card">
        </div>
        <div class="big-card card">
        <a id="link" href="https://www.linkedin.com/in/hasiow/" class="fill-div"></a>
        </div>
    </div>
</div>"")
