from flask_restful import Resource
from flask import request, render_template, make_response

class PriceCheckerResource(Resource):
    def post(self):
        
        try:
            json_data = request.form.get("search_item")
            from pricechecker.price_checker import start_price_checker
            result = start_price_checker(json_data)
            headers = {'Content-Type': 'text/html'}

            # return render_template("home2.html", result=result)
            return make_response(render_template("home2.html", result=result))

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500




# class PriceCheckerResourceJumia(Resource):
    
#     def post(self):
#         json_data = request.form.get("search_item")
#         print(json_data)

        
#         try:
#             from pricechecker.price_checker import start_price_checker,
#             jumia_data = check_jumia_price(json_data)
#             headers = {'Content-Type': 'text/html'}
#             flash("Finished scrapping Jumia. Now Scrapping Ali Express. Hang tight", "info")
#             return make_response(render_template("home.html"), headers), start_price_checker(json_data)

#         except Exception as e:
#             return {
#                 'status': 'failed',
#                 'data': None,
#                 'message': str(e)
#             }, 500






            
            