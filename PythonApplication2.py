import pandas as pd
import numpy as np

# 1. تحديد مسار الملف بداخل المجلد الحقيقي للمشروع
data_path = 'energy_efficient_dataset.csv'

try:
    # قراءة البيانات
    df = pd.read_csv(data_path)
    print("==================================================")
    print("✅ Data read successfully!")
    print("==================================================\n")
    
    # 2. عرض أول 5 صفوف من البيانات
    print("--- 1. First 5 Rows ---")
    print(df.head())
    print("\n" + "="*50 + "\n")
    
    # 3. فحص أنواع الأعمدة والقيم المفقودة (Null Values)
    print("--- 2. Dataset Info & Missing Values ---")
    df.info()
    print("\n" + "="*50 + "\n")
    
    # 4. ملخص إحصائي سريع للأرقام
    print("--- 3. Statistical Summary ---")
    print(df.describe().T)
    print("\n" + "="*50 + "\n")
    
    # 5. تحليل المتغير المستهدف (Multi-class Target: Efficiency_Class)
    if 'Efficiency_Class' in df.columns:
        print("--- 4. Target Variable Distribution (Efficiency_Class) ---")
        
        # التوزيع بالتكرار
        counts = df['Efficiency_Class'].value_counts()
        # التوزيع المئوي
        percentages = df['Efficiency_Class'].value_counts(normalize=True) * 100
        
        target_summary = pd.DataFrame({'Count': counts, 'Percentage (%)': percentages})
        print(target_summary)
        print("\n✅ المتغير المستهدف جاهز بـ 3 فئات (Multi-class).")
    else:
        print("⚠️ تنبيه: لم يتم العثور على عمود Efficiency_Class في البيانات.")

except Exception as e:
    print(f"❌ حدث خطأ أثناء قراءة البيانات: {e}")