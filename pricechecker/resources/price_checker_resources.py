from flask_restful import Resource
from flask import request, render_template, make_response


class PriceCheckerResource(Resource):
    
    def post(self):
        json_data = request.form.get("search_item")
        # print(f"{search_item},  is here now")
        # json_data = request.get_json()
        print(json_data)

        # req_fields = ["search_item"]

        # for field in req_fields:
        #     if field not in json_data:
        #         print(f"{field} is required")
        #         return {
        #             'status': 'failed',
        #             'data': None,
        #             'message': field + ' is required'
        #         }, 400
        #     elif json_data[field] == '':
        #         print(f"{field} cannot be empty")
        #         return {
        #             'status': 'failed',
        #             'data': None,
        #             'message': field + ' cannot be empty'
        #         }, 400
        #     else:
        #         pass


        try:
            from pricechecker.price_checker import start_price_checker

            # search_item = json_data['search_item']
            result = start_price_checker(json_data)
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template("home.html", result=result), headers)
            # return render_template('home.html', sample_input=sample_input, sample_output=sample_output), 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500






            
            