from flask_jwt_extended import create_access_token


class IdentificationService:

    def login(self, email, password):
        if email=="toto" and password =="tata":
            token = create_access_token("toto", additional_claims={"role":"client"})
            return token
        else:
            raise ValueError("Erreur email ou password")