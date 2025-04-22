let images = ["https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg", "https://npr.brightspotcdn.com/dims4/default/cf49d50/2147483647/strip/true/crop/7952x5304+0+0/resize/880x587!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fbb%2F0f%2Fd51269314ac39ea48c89439cd235%2Fjules-marvin-eguilos-xlnl6cwijng-unsplash.jpg", "https://worldwildschooling.com/wp-content/uploads/2024/01/Matterhorn_Mumemories_Adobe-Stock-Photo_682931585.jpg", "https://c02.purpledshub.com/uploads/sites/41/2021/08/GettyImages-484576000-c-bc46733.jpg", "https://hips.hearstapps.com/hmg-prod/images/the-jefferson-memorial-during-the-cherry-blossom-royalty-free-image-1621222377."]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("image").src = images[counter]
        counter += 1
    }else{
        counter = 0
        document.getElementById("image").src = images[counter]
    }

}

function hello(){
    document.getElementById("title").innerHTML = "HELLO WORLDDD!!"
}

function hover(){
    document.getElementById("image").src = "https://npr.brightspotcdn.com/dims4/default/cf49d50/2147483647/strip/true/crop/7952x5304+0+0/resize/880x587!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fbb%2F0f%2Fd51269314ac39ea48c89439cd235%2Fjules-marvin-eguilos-xlnl6cwijng-unsplash.jpg"
}

function leave(){
    document.getElementById("image").src = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg"
}

function hidden(){
    document.getElementById("meme").style.display = "block"
}