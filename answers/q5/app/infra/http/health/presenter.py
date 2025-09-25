class HealthPresenter:
    @staticmethod
    def toHTTP_ok() -> dict[str, str]:
        return {"status": "ok"}
