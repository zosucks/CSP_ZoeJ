let images = ["https://m.media-amazon.com/images/M/MV5BNGM1N2U3YmYtYjVlYi00YTAyLWI0MmMtMTRiZDczOTJiZWQ3XkEyXkFqcGc@._V1_.jpg", "https://ca-times.brightspotcdn.com/dims4/default/cb16b10/2147483647/strip/true/crop/4935x3290+0+0/resize/2400x1600!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F5b%2F33%2Ff367fb35474d864941e977e5f48e%2F927846-ca-0321-red-hot-chili-peppers-sunday-calendar-cover-mrt-02.jpg", "https://media.gq.com/photos/5dcf0c8db0d49b000820d449/16:9/w_2560%2Cc_limit/tyler-the-creator-gq-men-of-the-year-2019-01%2520(1).jpg", "https://cdn.shortpixel.ai/spai/q_lossy+ret_img+to_webp/joysauce.com/wp-content/uploads/2024/11/BoyWithUke-HERO-min.jpg", "https://traklife.com/wp-content/uploads/2023/02/jvke.jpg"]
counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("img").src = images[counter]
        counter += 1
    }else{
        counter = 0
        document.getElementById("img").src = images[counter]
    }

}

function view(){
    if(document.getElementById("add").style.display === "block"){
            document.getElementById("add").style.display = "none"
            document.getElementById("view").innerHTML = "Show more"
    }else{
        document.getElementById("add").style.display = "block"
        document.getElementById("view").innerHTML = "Show less"
    }
}