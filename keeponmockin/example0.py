def send_email(to, subject, body):
    pass


class CalculationEngine(object):
    def schedule_simulation(self, model):
        pass
    
    def wait_for_result(self, model):
        pass


def find_models(taggedwith):
    pass


def nightly_report(engine):
    models = find_models(taggedwith="nightly")
    
    for model in models:
        engine.schedule_simulation(model)
        
    failed = []
    for model in models:
        if not engine.wait_for_result(model):
            failed.append(model)
    
    send_email("support@example.com",
               "Nightly Report Status",
               "Ran {} models, {} failed.".format(len(models), len(failed)))
