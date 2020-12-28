 <code>
    pip install requirements.txt
    <br>
    python manage.py runsever

    <b>Live URL - https://jitfin.herokuapp.com/</b>

 </code>

Add querystring to the url username

/?username={githubusername}

<hr>
<pre>
                <p>Task 1</p>
            <code >
               API for getting user info | <b>add query string username</b>   <span class="badge badge-primary">ACCEPTS GET REQUEST</span>
               <kbd >/get?username={YOUR USERNAME}</kbd>
            </code>
            </pre>

<hr>

<pre>
                <p>Task 2</p>
                <code class="">
                   API for getting followers of a user | <b>add query string username</b>   <span class="badge badge-primary">ACCEPTS GET REQUEST</span>
                   <kbd >/followers?username={YOUR USERNAME}</kbd>
                </code>
                </pre>

<hr>
<pre>
                <p>Task 3</p>
                <code class="">
                   API for getting followers of a user | <b>add query string username</b>   <span class="badge badge-primary">ACCEPTS GET REQUEST</span>
                   <kbd >/followers?username={YOUR USERNAME}</kbd>
                </code>
                </pre>


<hr>

<pre>
                <p>Task 4</p>
                <code >API for creating new repository for a user  <span class="badge badge-danger">ACCEPTS POST REQUEST</span>
                <kbd >/create/</kbd>
                <code>
                    {
                    "token" : "{YOUR TOKEN}" , 
                    "name" : "{REPO NAME YOU WANT TO CREATE}" 
                    }
             </code>
             </pre>

<hr>
<pre>
                <p>Task 5</p>
             <code >API for update description of a repository. <span class="badge badge-success">ACCEPTS PATCH REQUEST</span>
                <kbd >/update/</kbd>
                <code>
                    {
                    "token" : "{YOUR TOKEN}" , 
                    "name" : "{USERNAME}" ,
                    "repo" : "{REPO NAME}" ,
                    "owner" : "{OWNER NAME}" ,
                    "description" : "{DESCRIPTION}"
                    }
                </code>


<hr>




</div>