# SubsidySeva - Government Subsidy Portal

A static HTML website that helps Indian citizens discover and access government and private subsidies with an authentic government portal-inspired design.

## Features

- **Static HTML Website** - No server required, can be hosted anywhere
- **15 Authentic Government Subsidies** - Real data sourced from official government websites
- **Responsive Design** - Mobile-friendly interface with Bootstrap 5
- **Advanced Search & Filtering** - Find subsidies by text search and category filters
- **Government Portal Design** - Inspired by MyGov India and Digital India aesthetics
- **Accessibility Compliant** - WCAG guidelines followed for inclusive design
- **Database Ready** - MySQL/PostgreSQL schema prepared for future migration

## Quick Start

### Option 1: Simple File Server
1. Download all files to a folder
2. Open `index.html` in any modern web browser
3. For full functionality, serve via HTTP (not file://)

### Option 2: Local Web Server

**Using Python:**
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

**Using Node.js:**
```bash
npm install -g http-server
http-server
```

**Using PHP:**
```bash
php -S localhost:8000
```

Then open http://localhost:8000 in your browser.

### Option 3: Deploy to Hosting
Upload all files to any web hosting service:
- GitHub Pages
- Netlify
- Vercel
- Any shared hosting provider

## File Structure

```
subsidyseva/
├── index.html              # Homepage
├── subsidies.html          # All subsidies listing page
├── suggest.html            # Suggest new scheme form
├── static/
│   ├── css/
│   │   └── style.css      # Custom styling with Indian government colors
│   └── js/
│       ├── subsidies-data.js  # 15 authentic government subsidies data
│       ├── main.js           # Homepage functionality
│       ├── subsidies.js      # Subsidies page functionality
│       └── suggest.js        # Suggestion form functionality
├── database_config.py      # MySQL/PostgreSQL configuration for future use
├── subsidies_database.sql  # Complete database schema
└── README.md              # This file
```

## Available Subsidies

The website includes 15 authentic government subsidies:

1. **Pradhan Mantri Awas Yojana (Urban)** - Housing assistance
2. **PM-KISAN** - Farmer income support
3. **Beti Bachao Beti Padhao** - Women empowerment
4. **National Scholarship Portal** - Student scholarships
5. **PM Vaya Vandana Yojana** - Senior citizen pension
6. **Stand-Up India** - Entrepreneur loans
7. **NHFDC** - Disabled persons support
8. **National Widow Pension** - Widow financial assistance
9. **PM Ujjwala Yojana** - LPG connections for women
10. **Atal Pension Yojana** - Pension for unorganized workers
11. **PM Suraksha Bima Yojana** - Accident insurance
12. **PM Fasal Bima Yojana** - Crop insurance
13. **PM Mudra Yojana** - Micro-finance loans
14. **Deendayal Antyodaya Yojana** - Rural livelihoods
15. **ICDS** - Child development services

## Database Migration (Future)

To convert to a database-driven application:

1. **MySQL Setup:**
   - Run the SQL schema from `subsidies_database.sql`
   - Update database credentials in `database_config.py`
   - Use the provided Flask/Django integration code

2. **PostgreSQL Setup:**
   - Modify schema for PostgreSQL compatibility
   - Update connection strings accordingly

## Customization

### Adding New Subsidies
Edit `static/js/subsidies-data.js` and add new subsidy objects to the `SUBSIDIES_DATA` array:

```javascript
{
    "id": 16,
    "title": "New Scheme Name",
    "description": "Detailed description",
    "eligibility": "Who can apply",
    "categories": ["Category1", "Category2"],
    "application_link": "https://official-link.gov.in",
    "amount": "Benefit amount",
    "department": "Responsible Ministry",
    "status": "Active"
}
```

### Styling Changes
- Colors: Edit CSS custom properties in `static/css/style.css`
- Layout: Modify Bootstrap classes in HTML files
- Icons: Change Font Awesome icons as needed

### Adding Categories
1. Add new category to subsidy data
2. Update category dropdowns in HTML files
3. Add corresponding category links on homepage

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Mobile)

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
- Government color scheme (Saffron, Green, Navy Blue)
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

## Support

For technical issues or subsidy data updates, please create an issue in the repository or contact the development team.

---

**Built for the citizens of India with pride** 🇮🇳