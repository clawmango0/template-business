# Template Pricing Data - Fiverr-style pricing tiers

PRICING_TIERS = {
    'starter': {
        'name': 'Starter',
        'price': 5,
        'delivery': '24 hours',
        'revisions': 1,
        'description': 'Basic template with company name customization'
    },
    'professional': {
        'name': 'Professional',
        'price': 25,
        'delivery': '48 hours',
        'revisions': 2,
        'description': 'Full customization plus logo placement'
    },
    'premium': {
        'name': 'Premium',
        'price': 75,
        'delivery': '72 hours',
        'revisions': 3,
        'description': 'Complete customization with industry-specific modifications'
    },
    'enterprise': {
        'name': 'Enterprise',
        'price': 150,
        'delivery': '1 week',
        'revisions': 5,
        'description': 'White-label with dedicated support'
    }
}

# Template to pricing tier mapping
TEMPLATE_PRICING = {
    # SOPs
    'onboarding': {'tier': 'starter', 'category': 'SOPs'},
    'incident_response': {'tier': 'professional', 'category': 'SOPs'},
    'change_management': {'tier': 'professional', 'category': 'SOPs'},
    'vendor_management': {'tier': 'starter', 'category': 'SOPs'},
    'data_backup': {'tier': 'professional', 'category': 'SOPs'},
    'saas_selection': {'tier': 'professional', 'category': 'SOPs'},
    'access_management': {'tier': 'professional', 'category': 'SOPs'},
    'physical_security': {'tier': 'professional', 'category': 'SOPs'},
    'saas_onboarding': {'tier': 'professional', 'category': 'SOPs'},
    
    # HR
    'employee_handbook': {'tier': 'premium', 'category': 'HR'},
    'job_description': {'tier': 'starter', 'category': 'HR'},
    'performance_review': {'tier': 'starter', 'category': 'HR'},
    'it_onboarding': {'tier': 'professional', 'category': 'HR'},
    
    # Project
    'project_charter': {'tier': 'starter', 'category': 'Project'},
    'status_report': {'tier': 'starter', 'category': 'Project'},
    'meeting_notes': {'tier': 'starter', 'category': 'Project'},
    'raci_matrix': {'tier': 'starter', 'category': 'Project'},
    'risk_register': {'tier': 'starter', 'category': 'Project'},
    'decision_log': {'tier': 'starter', 'category': 'Project'},
    'retrospective': {'tier': 'starter', 'category': 'Project'},
    
    # Finance
    'invoice': {'tier': 'starter', 'category': 'Finance'},
    'expense_report': {'tier': 'starter', 'category': 'Finance'},
    'budget_tracker': {'tier': 'starter', 'category': 'Finance'},
    'equipment_inventory': {'tier': 'starter', 'category': 'Finance'},
    
    # Executive
    'board_update': {'tier': 'premium', 'category': 'Executive'},
    'qbr': {'tier': 'professional', 'category': 'Executive'},
    'okr_tracker': {'tier': 'professional', 'category': 'Executive'},
    
    # Legal
    'nda': {'tier': 'professional', 'category': 'Legal'},
    'contractor_agreement': {'tier': 'premium', 'category': 'Legal'},
    'employment_offer': {'tier': 'professional', 'category': 'Legal'},
    'privacy_policy': {'tier': 'premium', 'category': 'Legal'},
    'terms_of_service': {'tier': 'professional', 'category': 'Legal'},
    'service_level_agreement': {'tier': 'premium', 'category': 'Legal'},
    'service_agreement': {'tier': 'professional', 'category': 'Legal'},
    'statement_of_work': {'tier': 'professional', 'category': 'Legal'},
    
    # Marketing
    'campaign_brief': {'tier': 'starter', 'category': 'Marketing'},
    'email_templates': {'tier': 'professional', 'category': 'Marketing'},
    'business_proposal': {'tier': 'professional', 'category': 'Marketing'},
    
    # Customer Success
    'success_plan': {'tier': 'professional', 'category': 'Customer Success'},
    
    # Operations
    'maintenance_log': {'tier': 'starter', 'category': 'Operations'},
    'shift_handover': {'tier': 'starter', 'category': 'Operations'},
    'client_onboarding': {'tier': 'professional', 'category': 'Operations'},
    
    # Healthcare
    'hipaa_policy': {'tier': 'enterprise', 'category': 'Healthcare'},
    
    # Construction
    'construction_checklist': {'tier': 'professional', 'category': 'Construction'},
    
    # Retail
    'store_opening': {'tier': 'professional', 'category': 'Retail'},
}

def get_template_price(template_slug):
    """Get price for a template"""
    tier = TEMPLATE_PRICING.get(template_slug, {}).get('tier', 'starter')
    return PRICING_TIERS.get(tier, PRICING_TIERS['starter'])
