from scraper import scrape

# Sample Query:
# Determine the demand for back-end web frameworks for developers:
web_frameworks = [
    'PHP Laravel',
    'Java Spring',
    'ASP .NET',
    'Ruby Rails',
    'Python Django',
    'Python Flask',
    'Node.js',
    ]

# Input format:
# scrape(keyword_list, 'filename.csv', job_title)
# job_title is used to filter out the results
# job_title is set as 'developer' to limit for developer jobs
scrape(web_frameworks, 'web_frameworks.csv', 'developer')
# Output the data to 'web_frameworks.csv'

languages = [
    'Python',
    'Golang',
    'Java',
    'C#',
    'Javascript',
    'Ruby',
    'Typescript',
    'PHP',
    'Rust',
    'Kotlin',
    'C++',
    'Swift',
    'Scala'
    ]
scrape(languages, 'programming.csv', 'developer')

front_end = [
    'React',
    'Angular',
    'Blazor',
    'Vue',
    'jQuery',
    'Ember',
    'Svelte',
    'Backbone.js'
    ]
scrape(front_end, 'frontend.csv', 'developer')

databases = [
    'PostgreSQL',
    'MySQL',
    'Microsoft SQL Server',
    'Oracle',
    'MariaDB',
    'MongoDB',
    'Redis',
    'Firebase'
    ]
scrape(databases, 'databases.csv', 'developer')
