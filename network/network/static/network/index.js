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
                poat.className = 'post-container'
                post.innerHTML = `
                    <a href="/profile/${post.creator}" style="color:black;"><h5>{{post_data.post.creator}}</h5></a>
                    <div class="comment-container">
                        <div style="white-space:pre-line" class="">{{post_data.post.body}}</div>
                        <p style="color:gray">{{post_data.post.timestamp}}</p>

                        {% if post_data.user_like %}
                        <button id="like-button-{{post_data.post.id}}" class="badge badge-primary" style="font-size:130%; border: none;">❤️ {{post_data.likes_num}}</button>
                        {% else %}
                        <button id="like-button-{{post_data.post.id}}" class="badge badge-light" style="font-size:130%; border: none;">❤️ {{post_data.likes_num}}</button>
                        {% endif %}
                    </div>

                    <div style="font-size:120%; margin-top:20px; margin-left:13px">Comments:</div>

                    <button id="show-comments-{{post_data.post.id}}" class="btn btn-link" style="margin:0px">Show comments</button>
                    <br>
                    <div id="comments-{{post_data.post.id}}" style="display:none">
                        {% for comment in post_data.comments %}
                        <div class="comment-container">
                            <p><b>{{comment.creator}}</b> --- <span style="color:gray">{{comment.timestamp}}</span><p>
                            <p style="white-space:pre-line">{{comment.body}}</p>
                        </div>
                        {% endfor %}
                        <textarea id="comment-text-{{post_data.post.id}}" style="display:none;margin-bottom:20px" class="form-control" rows="5" placeholder="Write your comment here"></textarea>
                        <span style="display:flex">
                            <button id="comment-button-{{post_data.post.id}}" class="btn btn-outline-primary">Comment</button>
                            &nbsp&nbsp&nbsp
                            <button id="cancel-button-{{post_data.post.id}}" class="btn btn-outline-primary" style="display:none">Cancel</button>
                        </span>
                    </div>
                `
            }
        })
    })
})
