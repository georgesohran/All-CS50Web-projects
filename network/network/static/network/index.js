document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('new-post-form').addEventListener('submit', (event) => {
        event.preventDefault()
        fetch('/api_make_post', {
                method:"POST",
                body:JSON.stringify({contents : document.getElementById('contents').value})
        }).then(response => response.json()).then((result) => {
            document.getElementById('message').innerHTML = result.message
            if('post' in result) {
                let post = document.createElement('div')
                post.className = 'post-container'
                post.innerHTML = `
                    <a href="/profile/${result.post.creator_id}" style="color:black;"><h5>{{post_data.post.creator}}</h5></a>
                    <div class="comment-container">
                        <div style="white-space:pre-line" class="">${result.post.body}</div>
                        <p style="color:gray">${result.post.timestamp}</p>

                        <button id="like-button-${result.post.id}" class="badge badge-light" style="font-size:130%; border: none;">❤️ 0</button>
                    </div>

                    <div style="font-size:120%; margin-top:20px; margin-left:13px">Comments:</div>

                    <button id="show-comments-${result.post.id}" class="btn btn-link" style="margin:0px">Show comments</button>
                    <br>
                    <div id="comments-${result.post.id}" style="display:none">
                        <textarea id="comment-text-${result.post.id}" style="display:none;margin-bottom:20px" class="form-control" rows="5" placeholder="Write your comment here"></textarea>
                        <span style="display:flex">
                            <button id="comment-button-${result.post.id}" class="btn btn-outline-primary">Comment</button>
                            &nbsp&nbsp&nbsp
                            <button id="cancel-button-${result.post.id}" class="btn btn-outline-primary" style="display:none">Cancel</button>
                        </span>
                    </div>
                `
                document.querySelector('posts').prepend(post)
            }
        })
    })
})
