## GitHub Profile Viewer

### Description:
The GitHub Profile Viewer is a Flask web application that allows users to view GitHub profiles along with user repositories. The application fetches data from the GitHub API using the provided access token and displays user information and repositories dynamically on a web page.


### Accessing Your GitHub Profile or How To Use

1. **Access the Application**: Go to [GitHub Card App](https://githubcardapp.vercel.app/) to access the application.

2. **Modify the URL**: Once on the application page, you'll notice the URL in the address bar. It may look something like `https://githubcardapp.vercel.app/`. To view your own GitHub profile, replace the default username (`arycodes`) in the URL with your GitHub username.

   For example:
   - If your GitHub username is `yourusername`, your URL should look like `https://githubcardapp.vercel.app/yourusername`.

3. **Press Enter or Go**: After replacing the default username with your GitHub username, press enter or click on the "Go" button in your browser to load the updated URL.

4. **View Your Profile**: The application will fetch your GitHub profile information based on the provided username and display it on the screen, including your user data and repositories.

5. **Explore Further**: Feel free to explore the data and repositories fetched from your GitHub profile.

By following these steps, users can easily replace the default username in the URL with their own GitHub username to view their profile information using the GitHub Card App.

## Features:
- Fetches user data including name, bio, email, company, location, followers, following, and avatar.
- Retrieves user repositories along with repository details such as name, description, language, URL, and languages used.
- Provides a clean and intuitive user interface for viewing GitHub profiles and repositories.

### Installation and Setup:
1. Clone the repository:
   ```
   git clone https://github.com/arycodes/github-profile-viewer.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up a `.env` file with your GitHub access token:
   ```
   apiaccesstoken=YOUR_GITHUB_ACCESS_TOKEN
   ```
4. Run the Flask application:
   ```
   python app.py
   ```
5. Open your web browser and navigate to `http://localhost:5000` to view the application.

### Usage:
- Upon accessing the application, you will be directed to the GitHub profile page of the default user "arycodes". You can replace "arycodes" in the URL to view other GitHub profiles.
- The profile page displays user information including profile picture, name, bio, company, location, email, number of repositories, followers, and following.
- Additionally, the page lists the user's repositories with details such as name, description, language, URL, and the languages used in each repository.
- Users can navigate between different GitHub profiles by modifying the URL accordingly.

### Technologies Used:
- Python (Flask)
- HTML
- CSS
- JavaScript

### Credits:
- The application utilizes the GitHub API for fetching user data and repositories.
- Flask is used as the web framework for building the application.
- HTML, CSS, and JavaScript are employed for designing and enhancing the user interface.

### Contribution:
Contributions to the project are welcome! Feel free to fork the repository, make changes, and submit pull requests for review.

### License:
This project is licensed under the [MIT License](LICENSE).
---
### Author:
Aryan - [GitHub Profile](https://github.com/arycodes)
---
