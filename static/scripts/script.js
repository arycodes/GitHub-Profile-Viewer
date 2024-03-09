
var userDataString = document.getElementById("userdata").innerText;
var userData = JSON.parse(userDataString);

var userReposString = document.getElementById("userrepos").innerText;
var userRepos = JSON.parse(userReposString);


function displayUserData(userData) {
    if (userData) {
        document.getElementById("avatar").src = userData.avatarUrl;
        document.getElementById("name").innerHTML = userData.name;
        document.getElementById("bio").innerHTML = userData.bio || '';

        if (userData.company) {
            document.getElementById("company").innerHTML = `Company: ${userData.company}`;
        } else {
            document.getElementById("company").innerHTML = '';
        }

        if (userData.location) {
            document.getElementById("location").innerHTML = `Location: ${userData.location}`;
        } else {
            document.getElementById("location").innerHTML = '';
        }

        if (userData.email) {
            document.getElementById("email").innerHTML = `Email: ${userData.email}`;
        } else {
            document.getElementById("email").innerHTML = '';
        }

        document.getElementById("following").innerHTML = userData.following;
        document.getElementById("followers").innerHTML = userData.followers;
        document.getElementById("repository").innerHTML = userData.publicRepos;

        document.getElementById("followbutton").onclick = function () {
            window.location.href = userData.githubUrl;
        };

        document.getElementById("username").innerHTML = "@" + userData.username;
    } else {
        console.log('Failed to fetch user data.');
    }
}




function createPostDivs(data) {
    var postContainer = document.getElementById("postcontainer");

    data.forEach(function (item) {
        var postDiv = document.createElement("div");
        postDiv.className = "post";

        var nameHeader = document.createElement("h2");
        nameHeader.textContent = item.name;

        var languagesParagraph = document.createElement("p");
        languagesParagraph.textContent = "Languages: " + (item.languages.length > 0 ? item.languages.join(", ") : "Not specified");

        var descriptionParagraph = document.createElement("p");
        descriptionParagraph.textContent = item.description ? item.description : "No description provided";

        var repositoryLink = document.createElement("a");
        repositoryLink.href = item.url;
        repositoryLink.target = "_blank";
        repositoryLink.textContent = "See Repository";

        postDiv.appendChild(nameHeader);
        postDiv.appendChild(languagesParagraph);
        postDiv.appendChild(descriptionParagraph);
        postDiv.appendChild(repositoryLink);

        postContainer.appendChild(postDiv);
    });
}



displayUserData(userData);
createPostDivs(userRepos);


document.querySelector(".toggleFormBtn").addEventListener("click", function () {
    var formContainer = document.getElementById("customFormContainer");
    formContainer.classList.toggle("active");
    if (formContainer.classList.contains("active")) {
        document.querySelector(".toggleFormBtn").textContent = "Close Form";
    } else {
        document.querySelector(".toggleFormBtn").textContent = "Create Your Own";
    }
});

document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault();

    var inputValue = document.getElementById("customInputField").value.trim();
    if (inputValue !== "") {
        window.location.href = "https://githubcardapp.vercel.app/" + inputValue;
    }
});
