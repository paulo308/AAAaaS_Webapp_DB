class Route:
    """ Routes names """
    # WEB routes
    HOME = "home"
    WEB = "home_web"
    WEB_CHECKIN = "checkin"
    WEB_CHECKOUT = "checkout"
    WEB_SIGNUP = "signup"
    WEB_SETTINGS = "settings"
    WEB_MANAGE_AUTH = "manage_info_auth"
    WEB_MANAGE_USER = "manage_info_user"
    WEB_MANAGE_ADMIN = "manage_info_admin"
    WEB_EMAIL_CONFIRMATION = "web_email_confirmation"
    WEB_SIGNIN_OPTIONS = "web_signin_options"
    # REST API routes
    GET_CHECKIN = "checkin_data"
    GET_CHECKOUT = "checkout_data"
    GET_SIGNUP = "signup_data"
    GET_VERIFY_TOKEN = "verify_token_data"
    GET_READ_USER_INFO = "read_user_info_data"
    GET_UPDATE_USER = "update_user_password_data"
    GET_CHANGE_PASSWORD = "change_password_data"
    GET_FORGOT_PASSWORD = "forgot_password_data"
    GET_DELETE_USER = "delete_user_data"
    GET_EMAIL_CONFIRMATION = "email_confirmation_data"
    GET_SEND_EMAIL_TOKEN = "send_email_token_data"
    GET_CREATE_AUTHORISATION = "create_authorisation_data"
    GET_READ_AUTHORISATION = "read_authorisation_data"
    GET_READ_AUTHORISATIONS = "read_authorisations_data"
    GET_UPDATE_AUTHORISATION = "update_authorisation_data"
    GET_DELETE_AUTHORISATION = "delete_authorisation_data"
    GET_USE_RESOURCE = "use_resource_data"
    GET_CREATE_EMAIL = "create_email_data"
    GET_READ_EMAILS = "read_emails_data"
    GET_DELETE_EMAIL = "delete_email_data"
    GET_CREATE_FAVORITE = "create_favorite_data"
    GET_READ_FAVORITE = "read_favorite_data"
    GET_READ_FAVORITES = "read_favorites_data"
    GET_DELETE_FAVORITE = "delete_favorite_data"
    GET_READ_ACCOUNTING = "read_accounting_data"
    # REST API routes
    CHECKIN = "checkin_state"
    CHECKOUT = "checkout_state"
    SIGNUP = "signup_state"
    VERIFY_TOKEN = "verify_token"
    READ_USER_INFO = "read_user_info"
    UPDATE_USER = "update_user"
    CHANGE_PASSWORD = "change_password"
    FORGOT_PASSWORD = "forgot_password"
    DELETE_USER = "delete_user"
    EMAIL_CONFIRMATION = "email_confirmation"
    SEND_EMAIL_TOKEN = "send_email_token"
    CREATE_AUTHORISATION = "create_authorisation"
    READ_AUTHORISATION = "read_authorisation"
    READ_AUTHORISATIONS = "read_authorisations"
    UPDATE_AUTHORISATION = "update_authorisation"
    DELETE_AUTHORISATION = "delete_authorisation"
    USE_RESOURCE = "use_resource"
    CREATE_EMAIL = "create_email"
    READ_EMAILS = "read_emails"
    DELETE_EMAIL = "delete_email"
    CREATE_FAVORITE = "create_favorite"
    READ_FAVORITE = "read_favorite"
    READ_FAVORITES = "read_favorites"
    DELETE_FAVORITE = "delete_favorite"
    READ_ACCOUNTING = "read_accounting"
    # json routes
    CHECKIN_STATE = "get_checkin_state"
    CHECKOUT_STATE = "get_checkout_state"
    SIGNUP_STATE = "get_signup_state"
    # static assets routes
    STATIC_ASSETS = "static"