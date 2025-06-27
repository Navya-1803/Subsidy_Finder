# SubsidySeva - Subsidy Portal

A static HTML website that helps Indian citizens discover and access government and private subsidies with an authentic government portal-inspired design.

## Features

- **Static HTML Website** - No server required, can be hosted anywhere
- **15 Authentic Government Subsidies** - Real data sourced from official government websites
- **Responsive Design** - Mobile-friendly interface with Bootstrap 5
- **Advanced Search & Filtering** - Find subsidies by text search and category filters
- **Government Portal Design** - Inspired by MyGov India and Digital India aesthetics
- **Accessibility Compliant** - WCAG guidelines followed for inclusive design
- **Database Ready** - MySQL/PostgreSQL schema prepared for future migration

## File Structure

```
subsidyseva/
├── index.html              # Homepage
├── subsidies.html          # All subsidies listing page
├── suggest.html            # Suggest new scheme form
├── static/
│   ├── css/
│   │   └── style.css      # Custom styling with Indian Flag colors
│   └── js/
│       ├── subsidies-data.js  # Government subsidies data
│       ├── main.js           # Homepage functionality
│       ├── subsidies.js      # Subsidies page functionality
│       └── suggest.js        # Suggestion form functionality
├── database_config.py      # MySQL/PostgreSQL configuration for future use
├── subsidies_database.sql  # Complete database schema
└── README.md              # This file
```

## Database Migration (Future)

To convert to a database-driven application:

1. **MySQL Setup:**
   - Run the SQL schema from `subsidies_database.sql`
   - Update database credentials in `database_config.py`
   - Use the provided Flask/Django integration code

2. **PostgreSQL Setup:**
   - Modify schema for PostgreSQL compatibility
   - Update connection strings accordingly


## Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Custom properties, Grid, Flexbox
- **JavaScript ES6+** - Modern JS features
- **Bootstrap 5.3** - Responsive framework
- **Font Awesome 6.4** - Icons
- **Google Fonts** - Typography (Open Sans, Roboto)

## Government Portal Compliance

The design follows Indian government web standards:
- Accessibility guidelines (WCAG 2.1)
- Indian flag color scheme (Saffron, Green, Navy Blue)
- Clean, professional layout
- Mobile-first responsive design
- Fast loading times
- SEO-friendly structure

## Future Enhancements

- User authentication system
- Personalized recommendations
- Multi-language support (Hindi, regional languages)
- Integration with government APIs
- Advanced analytics
- Mobile app version

## Contributing

1. Fork the repository
2. Add new authentic subsidy data with proper verification
3. Ensure all changes maintain government portal aesthetics
4. Test across different browsers and devices
5. Submit pull request with detailed description

## License

This project is created for public service and educational purposes. Government subsidy data is sourced from official websites and remains property of respective government departments.
