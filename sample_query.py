from scraper import scrape

# Sample Query:
# Determine the demand for back-end web frameworks for developers:
web_frameworks = {
    'Laravel': [],  # leaving the keywords blank is allowed
    'Spring': ['spring', 'springboot'],
    'ASP.NET': ['asp .net', 'asp.net', '.net core'],
    'Ruby on Rails': [],
    'Django': [],
    'Flask': [],
    'Express': ['node', 'node.js', 'mern', 'express.js']
}
# job_title is 'developer'
# job_title is used to filter out the results
scrape(web_frameworks, 'web_frameworks.csv', 'developer')
# Output the data to 'web_frameworks.csv'

front_end = {
    # React keywords will include atleast one of the 3:
    'React': ['React.js', 'React', 'ReactJS'],
    'Angular': ['Angular', 'Angular.js', 'AngularJS'],
    'Blazor': [],
    'Vue': ['Vue', 'Vue.js', 'VueJS'],
    'jQuery': [],
    'Ember': ['Ember.js', 'Ember', 'EmberJS'],
    'Meteor': ['Meteor.js', 'Meteor', 'MeteorJS'],
    'Svelte': [],
    'Backbone': ['Backbone JS', 'BackboneJS', 'Backbone.js']
}
scrape(front_end, 'frontend.csv', 'developer')

databases = {
    'PostgreSQL': ['pgSQL', 'PostgreSQL', 'Postgres', 'Postgre'],
    'MySQL': [],
    'Microsoft SQL Server': [
        'MSSQL', 'MS SQL', 'SQL Server', 'Microsoft SQL'
    ],
    'Oracle': ['OracleDB', 'Oracle Database'],
    'MariaDB': ['Maria DB', 'MariaDB'],
    'MongoDB': ['MongoDB', 'Mongo DB'],
    'Redis': [],
    'Firebase': []
}
scrape(databases, 'databases.csv', 'developer')

languages = {
    'Python': [],
    'Go': [
        'Go developer', 'Golang', 'Go Language', 'Go lang '
    ],
    'Java': [],
    'C#': ['c sharp', 'C#'],
    'Javascript': [],
    'Ruby': [],
    'Typescript': [],
    'PHP': [],
    'Rust': [],
    'Kotlin': [],
    'C++': [],
    'Swift': [],
    'Scala': []
}
scrape(languages, 'programming.csv', 'developer')

web_design = {
    'Figma': [],
    'Material UI': ['materialui', 'material ui'],
    'Bootstrap': [],
    'Photoshop': [],
    'Webflow': [],
    'Adobe XD': [' XD ', 'AdobeXD', 'Adobe XD'],
    'Illustrator': [],
    'SASS': ['SASS', 'SCSS'],
}
scrape(web_design, 'web_design.csv', 'web design')
