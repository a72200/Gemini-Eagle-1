import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# إعداد ذكاء جيميناي المستند إلى سحابة جوجل
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

app = FastAPI(title="Gemini Law Agent - Seven Worlds")

class CaseRequest(BaseModel):
    case_details: str
    opponent_argument: str

@app.post("/analyze_case")
async def analyze_case(request: CaseRequest):
    """
    تحليل القضايا القانونية، تنبؤ أحكام الخصوم، وصياغة المذكرات الأولية.
    """
    try:
        # استخدام نموذج Gemini 1.5 Pro لقدرته العميقة على التحليل القانوني
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = f"""
        أنت الآن "جيمني المحاماة" الروبوت القانوني الذكي في مشروع العوالم السبع.
        قم بتحليل القضية التالية وصياغة مذكرة دفاع أولية وتنبؤ بنقاط ضعف الخصم:
        
        تفاصيل القضية:
        {request.case_details}
        
        حجج الخصم:
        {request.opponent_argument}
        """
        
        response = model.generate_content(prompt)
        return {"status": "success", "legal_analysis": response.text}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
      
