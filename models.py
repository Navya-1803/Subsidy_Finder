from datetime import datetime
from app import db

class Subsidy(db.Model):
    __tablename__ = 'subsidies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    eligibility = db.Column(db.Text, nullable=False)
    application_link = db.Column(db.String(500))
    amount = db.Column(db.String(255))
    department = db.Column(db.String(255))
    status = db.Column(db.String(50), default='Active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to categories
    categories = db.relationship("SubsidyCategory", back_populates="subsidy", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'eligibility': self.eligibility,
            'application_link': self.application_link,
            'amount': self.amount,
            'department': self.department,
            'status': self.status,
            'categories': [cat.category for cat in self.categories]
        }

class SubsidyCategory(db.Model):
    __tablename__ = 'subsidy_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    subsidy_id = db.Column(db.Integer, db.ForeignKey('subsidies.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    
    # Relationship to subsidy
    subsidy = db.relationship("Subsidy", back_populates="categories")

class Suggestion(db.Model):
    __tablename__ = 'suggestions'
    
    id = db.Column(db.Integer, primary_key=True)
    scheme_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    eligibility = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    benefits = db.Column(db.String(255))
    contact_name = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255))
    contact_phone = db.Column(db.String(20))
    status = db.Column(db.String(50), default='Pending')
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'scheme_name': self.scheme_name,
            'description': self.description,
            'eligibility': self.eligibility,
            'category': self.category,
            'benefits': self.benefits,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'status': self.status,
            'submitted_at': self.submitted_at.isoformat() if self.submitted_at else None
        }