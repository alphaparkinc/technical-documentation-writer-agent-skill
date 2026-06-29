import sys
from doc_writer import TechnicalDocWriterClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Technical Documentation Writer Agent Example ===")
    client = TechnicalDocWriterClient()
    
    code = (
        "class OrderProcessor(BaseProcessor):\n"
        "    def execute_payment(self, amount: float) -> bool:\n"
        "        pass\n"
    )
    
    docs = client.write_documentation(code)
    print("\n--- Generated Markdown Reference ---")
    print(docs)

if __name__ == "__main__":
    main()
