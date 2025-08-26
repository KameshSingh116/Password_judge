# Password_judge
A basic python program to check the strength of the  password...

Here's the GitHub-ready Markdown file for your password strength analyzer.

Password Strength Analyzer 🔐
This is a simple Python script that analyzes the strength of a password based on several criteria, including length and the inclusion of lowercase letters, uppercase letters, numbers, and special characters.

Features ✨
Length Check: Awards points for longer passwords.

Character Variety: Checks for a mix of character types (lowercase, uppercase, numbers, and special symbols).

Scoring System: Assigns a numerical score to the password, rating it as weak, medium, or strong.

Feedback: Provides suggestions for improving password strength.

File Logging: If a password is rated as "High" strength, it's saved to a file named passwords.txt.

How It Works 💡
The script calculates a score for the password based on these rules:

Condition	Points Added
Length > 8 characters	+3
Length > 5 and <= 8 characters	+2
Length > 0 and <= 5 characters	+1
Contains at least one lowercase letter	+1
Contains at least one uppercase letter	+1
Contains at least one number	+1
Contains at least one special character	+1
The final score determines the password's strength rating:

Score <= 2: Weak

Score > 2 and <= 5: Medium

Score > 5: Strong
