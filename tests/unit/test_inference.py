def test_content_generation():
    generator = ContentGenerator()
    output = generator.generate("Hello", max_length=10)
    assert isinstance(output, str)