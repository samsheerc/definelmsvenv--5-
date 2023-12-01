let videoList = document.querySelectorAll('.video-list-container .list');

videoList.forEach(vid =>{
   vid.onclick = () =>{
      videoList.forEach(remove =>{remove.classList.remove('active')});
      vid.classList.add('active');
      let src = vid.querySelector('.list-video').src;
      let title = vid.querySelector('.list-title').innerHTML;
      document.querySelector('.main-video-container .main-video').src = src;
      document.querySelector('.main-video-container .main-video').play();
      document.querySelector('.main-video-container .main-vid-title').innerHTML = title;
   };
});


// /*
// 🎬 Video playlist UI Design like Skillshare With Vanilla JavaScript
// 👨🏻‍⚕️ By: Coding Design

// You can do whatever you want with the code. However if you love my content, you can subscribed my YouTube Channel
// 🌎link: www.youtube.com/codingdesign
// */

// function comment(){
    
//    const selectElement = document.querySelector('input[name="selectedvalue"]');
//    const comment = document.querySelector('input[name="comment"]');
//    alert(selectElement.value);
//    alert(comment.value);
// }
// const main_video = document.querySelector('.main-video iframe');
// const main_video_title = document.querySelector('.main-video .title');
// const video_playlist = document.querySelector('.video-playlist .videos');
// //const id_textfield = document.querySelector('.main-video id');
// const selectElement = document.querySelector('input[name="selectedvalue"]');


// let data = [
   
//    {
//        'id': 'a1',
//        'title': 'manipulate text background',
//        'name': 'manipulate text background.mp4',
//        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
//        'duration': '2:47',
//    }];
// //    {
// //        'id': 'a2',
// //        'title': 'build gauge with css',
// //        'name': 'build gauge with css.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '2:45',
// //    },
// //    {
// //        'id': 'a3',
// //        'title': '3D popup card',
// //        'name': '3D popup card.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '24:49',
// //    },

// //    {
// //        'id': 'a4',
// //        'title': 'customize HTML5 form elements',
// //        'name': 'customize HTML5 form elements.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '3:59',
// //    },
// //    {
// //        'id': 'a5',
// //        'title': 'custom select box',
// //        'name': 'custom select box.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '4:25',
// //    },
// //    {
// //        'id': 'a6',
// //        'title': 'embed google map to contact form',
// //        'name': 'embed google map to contact form.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '5:33',
// //    },
// //    {
// //        'id': 'a7',
// //        'title': 'password strength checker javascript web app',
// //        'name': 'password strength checker javascript web app.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '0:29',
// //    },

// //    {
// //        'id': 'a8',
// //        'title': 'custom range slider',
// //        'name': 'custom range slider.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',
// //        'duration': '1:12',
// //    },
// //    {
// //        'id': 'a9',
// //        'title': 'animated shopping cart',
// //        'name': 'animated shopping cart.mp4',
// //        'url':'https://www.youtube.com/embed/0T6_vtbO4aY',

// //        'duration': '3:38',
// //    },

// // ];

// data.forEach((video, i) => {
//    let video_element = `
//                <div class="video" data-id="${video.id}">
//                    <img src="images/play.svg" alt="">
//                    <p>${i + 1 > 9 ? i + 1 : '0' + (i + 1)}. </p>
//                    <h3 class="title">${video.title}</h3>
//                    <p class="time">${video.duration}</p>
//                </div>
//    `;
//    video_playlist.innerHTML += video_element;
// })

// let videos = document.querySelectorAll('.video');

// videos[0].classList.add('active');
// videos[0].querySelector('img').src ="https://img.icons8.com/ios-glyphs/30/null/pause--v1.png";

// videos.forEach(selected_video => {
//    selected_video.onclick = () => {
      
//        for (all_videos of videos) {

//            all_videos.classList.remove('active');
//            all_videos.querySelector('img').src ="https://img.icons8.com/ios-glyphs/30/null/play-button-circled--v1.png";

//        }

//        selected_video.classList.add('active');
//        selected_video.querySelector('img').src ="https://img.icons8.com/ios-glyphs/30/null/pause--v1.png";

//        let match_video = data.find(video => video.id == selected_video.dataset.id);
//        //main_video.src = 'videos/' + match_video.name;
      
//        main_video.src=match_video.url;
//        selectElement.value=match_video.id;
//       // document.getElementById("id").value="hiii";
//         main_video_title.innerHTML = match_video.title;
//    }
// });








(function($, document) {
    
   // get tallest tab__content element
   let height = -1;

   $('.tab__content').each(function() {
      height = height > $(this).outerHeight() ? height : $(this).outerHeight();
      $(this).css('position', 'absolute');
   });
   
   // set height of tabs + top offset
   $('[data-tabs]').css('min-height', height + 40 + 'px');

}(jQuery, document));